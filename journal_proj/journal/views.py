from django.shortcuts import render
from .models import Users, Trade, Trade_close
from  django.views.generic import FormView, TemplateView, View
from .forms import RegForm


class Reg (TemplateView):
    template_name = 'journal/reg.html'
    # context_object_name = 'users'

    def get_context_data(self,*args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        users = Users.objects.all()
        context['users'] = users
        context['count'] = users.count()
        context['login'] = users.values_list("login", flat=True)
        return context

    def post(self, request, *args, **kwargs):
        input_log = request.POST.get('login')
        input_pas = request.POST.get('password')
        users = Users.objects.all()
        context = self.get_context_data(*args,**kwargs)
        context['count'] = users.count()
        if input_log != None:
            print('first', input_log)
            # if len(users.values_list("login", flat=True))== 0:
            if context['count'] == 0:
                # print('IF-SECOND', input_log)
                context['success'] = "Успешная регистрация"
                new_user = Users(login=input_log, password=input_pas)
                new_user.save()
            else:
                print('IF-SECONDSECONDSECOND', input_log)
                # d=len(users.values_list("login", flat=True))
                for log in range(0,context['count']):
                    # uniq = True
                    print('сработало True')
                    print(log)
                    if str(input_log) == str(users[log].login):
                        print('third', input_log)
                        # uniq = False
                        print('сработало False')
                        context['success'] = "Такой логин уже существует"
                        break
                else:
                    print('сработало TRUE....................')
                    context['success'] = "Успешная регистрация"
                    new_user = Users(login=input_log, password=input_pas)
                    new_user.save()
                    context['count'] = users.count()
        # else:
        #     context['success'] = " не сработал метод  if input_log != None:"
        return render(request, self.template_name, context)


class Authoriz(TemplateView):
    template_name = 'journal/auth.html'

    def get_context_data(self,*args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        return context

    def post(self,request,*args, **kwargs ):
        context = self.get_context_data(*args, **kwargs)
        input_log = request.POST.get('login')
        input_pas = request.POST.get('password')
        context['auth_f']=False
        if input_log != None:
            try:
                global user
                user = Users.objects.get(login=input_log, password=input_pas)
                context['success_auth'] = "Успешная авторизация. Пройдите в главное меню."
                context['auth_f']=True
            except:
                context['success_auth'] = "Неверный пароль и логин"
        else:
            context['success_auth'] = "КОНЕЦ "
        return render(request, self.template_name, context)


class Main(TemplateView):
    template_name = 'journal/main.html'

    def get_context_data(self,*args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name)


class Writing(TemplateView):
    template_name = 'journal/write.html'

    def get_context_data(self,*args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)

        return context

    def post(self,request, *args,  **kwargs):
        context = self.get_context_data(*args,  **kwargs)
        context['tr_list'] = user.trade_set.all()
        s_name = request.POST.get('secur_name')
        id_tr = request.POST.get('id_trade')
        price_op = request.POST.get('price_open')
        price_cl = request.POST.get('price_close')
        quan_op = request.POST.get('quantity_open')
        quan_cl = request.POST.get('quantity_close')
        date_op = str(request.POST.get('calendar_open')) + ' ' + str(request.POST.get('calendar_time_open'))
        date_cl = str(request.POST.get('calendar_close')) + ' ' + str(request.POST.get('calendar_time_close'))

        if request.POST.get('price_open')!=None:
            trade_op = user.trade_set.create(secur_name=s_name, price_open=price_op, quantity_open=quan_op, date=date_op)
            print('secur_name', s_name)
            trade_op.save()
            context['tr_list'] = user.trade_set.all()
        if request.POST.get('price_close')!=None:
            trade_op = user.trade_set.get(pk=id_tr)
            trade_cl = trade_op.trade_close_set.create(price_close=price_cl, quantity_close=quan_cl, date=date_cl)
            print('price_close', price_cl)
            trade_cl.save()
        return render(request, self.template_name, context)


class Read_jour(TemplateView):
    template_name = 'journal/jour.html'

    def get_context_data(self,*args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        context['trade_op'] = user.trade_set.all()
        return render(request, self.template_name, context)