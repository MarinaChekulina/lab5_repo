from django.shortcuts import render


# Create your views here.
# def base(request):
#     return render(request, 'lab/base.html', {})

def main(request):
    return render(request, 'lab/main.html', {})


def sales(request):
    info1 = [
        {'id': '1',
         'name': 'Зимние шины в подарок при покупке автомобиля от 1,5 млн. руб.',
         'text': ''},
        {'id': '2',
         'name': 'КАСКО без процентов при покупке до 20 декабря 2016',
         'text': ''},
        {'id': '3',
         'name': 'Скидка 3% на автомобили 2015 года выпуска',
         'text': ''}
    ]
    return render(request, 'lab/sales.html', {'menu': info1})


def model_row(request):
    info2 = [
        {'id':'1',
         'name': 'Nissan Juke',
         'text': ' Цена от:100000 руб'},
        {'id':'2',
         'name': 'Nissan Qashqai',
         'text': 'Цена от:1250000 руб'},
        {'id':'3',
         'name': 'Nissan X-Trail',
         'text': 'Цена от:1450000 руб'},
        {'id':'4',
         'name': 'Nissan Murano',
         'text': 'Цена от:2150000 руб'},
        {'id':'5',
         'name': 'Nissan GT-R',
         'text': 'Цена от:6700000 руб'}
    ]
    return render(request, 'lab/model_row.html',{'menu': info2})


def address(request):
    info3 = [
        {'id': '11',
         'name': 'АВТОМИР',
         'adr':'Адрес: М. ЩЕЛКОВСКАЯ, 105-Й КМ МКАД (ВНЕШНЯЯ СТОРОНА), МКРН 1 МАЯ, Д. 14,МОСКВА,143900',
         'time':'ЕЖЕДНЕВНО С 9:00 ДО 21:00',
         'phone':'ТЕЛЕФОН: +7(495) 525-77-77'},
        {'id': '12',
         'name': 'АВТОЦЕНТР НА ТАГАНКЕ',
         'adr':'М. ТАГАНСКАЯ, УЛ. МАРКСИСТСКАЯ, Д. 34, МОСКВА,109147',
         'time':'ПОНЕДЕЛЬНИК-ПЯТНИЦА С 9.00 ДО 21.00, СУББОТА-ВОСКРЕСЕНИЕ С 9.00 ДО 20.00',
         'phone':' ТЕЛЕФОН: +7(495) 989-70-70'
    },
        {'id': '13',
         'name': 'NATC GROUP',
         'adr': 'М. РЯЗАНСКИЙ ПРОСПЕКТ, 2-Й ВЯЗОВСКИЙ ПР-Д, Д. 12, МОСКВА, 109428',
         'time': 'ЕЖЕДНЕВНО С 7:30 ДО 21:00',
         'phone': 'ТЕЛЕФОН: +7(495) 225-21-21'
         },
        {'id': '14',
         'name': 'GENSER',
         'adr': 'М. ДМИТРОВСКАЯ, УЛ. ДОБРОЛЮБОВА, Д. 2Б, МОСКВА, 127254',
         'time': 'ЕЖЕДНЕВНО С 8:00 ДО 22:00',
         'phone': 'ТЕЛЕФОН: +7(495) 786-20-50'
         }

    ]
    return render(request, 'lab/address.html', {'menu': info3})
