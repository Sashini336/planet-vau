# myapp/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'myapp/base.html')


def my_view(request):
    context = {
        "hotel": "100 Rizes Seaside Resort",
        "address_hotel": "23200 Gytheio, Gytheio, Greece",
        "main_image": "https://planet-media.s3.amazonaws.com/images/861162_56090437",
        "images": ['https://planet-media.s3.amazonaws.com/images/861162_32887839',
                   'https://planet-media.s3.amazonaws.com/images/861162_22006991',
                   'https://planet-media.s3.amazonaws.com/images/861162_11104790',
                   'https://planet-media.s3.amazonaws.com/images/861162_93451308'],
        'hotel_base': 'Повечето етажи са достъпни с помощта на асансьор. Към удобствата спадат съхранение на багаж и сейф. В общите части има безжичен достъп до интернет (без допълнително заплащане). Предлага се избор от различни заведения за хранене, като ресторант и кафене. Всичко това се допълва от градина. Пристигналите с автомобил могат да ползват паркинга на хотела (без допълнително заплащане). Детегледачка, трансфер и обслужване по стаите ще задоволят нуждите и на по-взискателните посетители.',
        'accommodation': 'В хотелската база са на разположение стаи с климатик, централно отопление и санитарен възел. За приятната атмосфера на много от хотелските единици допринася и красивата морска гледка. Гостите могат да спят удобно на легло с кралски размер. За най-малките посетители са налице бебешки кошарки. Освен това има сейф. В кухненската ниша се намират мини-хладилник и машина за приготвяне на чай или кафе. Оборудването включва още интернет достъп, телефон, телевизор и безжичен интернет. Комфортът в стаите се допълва от домашни пантофи. В санитарните възли ежедневно са на разположение сешоар и халати за баня. Възможно е да бъдат резервирани стаи със санитарни възли, пригодени за хора в инвалидни колички.',
        'entertainment': "През горещите дни от годината гостите могат да се освежат в изградените за тази цел външен и вътрешен басейн. Лятна градина и тераса правят почивката перфектна. Многообразие осигуряват различни оферти за свободното време, сред които фитнес-студио, СПА, сауна и масажни процедури.",
        'food': 'Гостите могат да избират между закуска, обяд или вечеря.',
        'reservertion-_ype': 'BB-Закуска',
        'type_room': 'Standard Double room (shared bathroom) (full double bed)',
        'price_includes': 'Без такса за анулиране до 02 яну 2024 23:00',
        'price_not_included': '',
        'cancelattion': 'Без възможност за анулация',
        'amount_people': '2 Възрастни + 1 дете',
        'net_price': 'EUR 26',
        'tax': '',
        'city_tax': 'BGN 0.8',
        'total': 'EUR 26'
    }

    return render(request, 'myapp/base.html', context)
