import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import LoginForm, RegistrationForm, SubscribersForm
from .models import Advertising, MainInfo, Coins
from datetime import date, datetime, timedelta, timezone


def index(request):
    advertisings = Advertising.objects.all()
    main_info = MainInfo.objects.all()
    coins = Coins.objects.all()
    context = {
        'advertisings': advertisings,
        'main_info': main_info,
        'coins': coins,
    }
    return render(request, 'index.html', context)


class CurrencyView(APIView):
    def get(self, request):
        objects = requests.get('https://www.binance.com/api/v3/ticker/24hr?symbols=[%22BTCUSDT%22,%22ETHUSDT%22,%22LTCUSDT%22]').json()
        context = {}
        for item in objects:
            context[item['symbol']] = ('$' + str(int(float(item['lastPrice']))), float(item['priceChangePercent'][:4]), '$' + str(int(float(item['quoteVolume']))))
        return Response(context)


class CalculateView(APIView):
    def get(self, request):
        coins = {
            'Bitcoin': '1',
            'Litecoin': '4'
        }
        hashrate = request.GET.get('hash')
        coin_id = coins[request.GET.get('coin')]
        objects = requests.get(f'https://whattomine.com/coins/{coin_id}.json?hr={hashrate}&p=2800.0&fee=0.0&cost=0&cost_currency=USD&hcost=0.0&span_br=1h&span_d=').json()
        return Response((objects['estimated_rewards'], objects['tag'], objects['profit']))


class GraphView(APIView):
    def get(self, request):
        coin = request.GET.get('coin').lower()
        currency = 'usd'
        dates = []
        result = []
        today = datetime.today() - timedelta(1)
        today_str = str(today).split(' ')[0]
        today_second = list(map(int, today_str.split('-')))
        end = datetime(today_second[0], today_second[1], today_second[2]).replace(tzinfo=timezone.utc).timestamp()
        start_str = str(today - timedelta(6)).split(' ')[0]
        start_lst = list(map(int, start_str.split('-')))
        start = datetime(start_lst[0], start_lst[1], start_lst[2]).replace(tzinfo=timezone.utc).timestamp()
        count = 6
        while count >= 0:
            dates.append(str(today - timedelta(count)).split(' ')[0])
            count -= 1
        objects = requests.get(
            f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range?vs_currency={currency}&from={start}&to={end}').json()
        objectlistres = []
        for item in objects['prices']:
            objectlistres.append(int(float(str(item[1])[:5])))
        flag = len(objectlistres) // 7
        prices = objectlistres[flag - 1::flag]
        for i in prices:
            result.append([dates[prices.index(i)], prices[prices.index(i)]])
        return Response(result)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/.')
                else:
                    return HttpResponse('Аккаунт неактивен')
            else:
                return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})


def subscribers(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/.')
    else:
        form = SubscribersForm()

    context = {'form': form}
    return render(request, 'feedback.html', context)
