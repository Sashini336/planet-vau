# myapp/views.py
from django.shortcuts import render


def get_hotel_rating():

    return 4.5


def get_people_counts():
    adult_count = 2
    child_count = 1
    return adult_count, child_count


def home(request):

    hotel_rating = get_hotel_rating()

    adult_count, child_count = get_people_counts()

    adult_icons = ['fa-solid fa-person fa-2xl' for _ in range(adult_count)]
    child_icons = ['fa-solid fa-child fa-xl' for _ in range(child_count)]

    context = {
        "hotel": "100 Rizes Seaside Resort",
        "address_hotel": "23200 Gytheio, Gytheio, Greece",
        "main_image": "https://planet-media.s3.amazonaws.com/images/861162_56090437",
        "images": ['https://planet-media.s3.amazonaws.com/images/861162_32887839',
                   'https://planet-media.s3.amazonaws.com/images/861162_22006991',
                   'https://planet-media.s3.amazonaws.com/images/861162_11104790',
                   'https://planet-media.s3.amazonaws.com/images/861162_93451308'],
        'about_hotel': '<h5>Хотелска база</h5><p>За гостите са налични фоайе и рецепция. Удобствата включват ресторант, бар и пералня. Гостите биха могли чрез безжичен достъп да сърфират в интернет пространството и да са в постоянен досег с глобалната мрежа. Всичко това се допълва от градина.</p><h5>Настаняване</h5><p>В този хотел са на разположение стаи с климатик, централно отопление и санитарен възел. Гостите на хотелската база получават за добре дошли комплименти (подарък). Балкон или тераса са стандарт в повечето стаи. Освен това могат да се ползват сейф и минибар. Към стандартното оборудване принадлежи също машина за приготвяне на чай или кафе. Пълноценната почивка се гарантира от телевизор, CD-устройство и безжичен интернет. Комфортът в стаите се допълва от домашни пантофи. За ежедневно ползване в санитарните възли са на разположение сешоар и халати за баня. Хотелът предлага фамилна стая и стаи за непушачи.</p><h5>Спорт/забавления</h5><p>През горещите дни от годината гостите могат да се освежат в изградените за тази цел външен и вътрешен басейн. Налична е също тераса с шезлонги и чадъри. Освен това до басейна е наличен бар. За всички, които искат да заложат на движението и активната почивка, се предлагат велосипеди под наем и стрелба с лък. С каране на водни ски, уиндсърфинг, ветроходство, катамаран, плаване с каяк, гмуркане с шнорхел и водолазно гмуркане ще останат задоволени очакванията и на любителите на водните спортове. Почиващи са поканени да опитат отличните възможности за активна почивка на хотела, сред които са фитнес-студио и йога. В хотелската база се предлагат различни възможности за релаксиране, сред които СПА, сауна, парна баня, козметичен салон, масажни процедури и процедури за подмладяване. Copyright GIATA 2004 - 2023. Multilingual, powered by www.giata.com for client no. 128106</p><h5>Хранене</h5><p>Гостите могат да избират между закуска, обяд и вечеря. Хотелът осигурява допълнително леки закуски. Налични са безалкохолни напитки и алкохол.</p>',
        'reservertion_type': 'BB-Закуска',
        'type_room': 'Standard Double room (shared bathroom) (full double bed)',
        'price_includes': 'Без такса за анулиране до 02 яну 2024 23:00',
        'price_not_included': '',
        'cancelattion': 'Без възможност за анулация',
        'amount_people': '2 Възрастни + 1 дете',
        'adult_icons': adult_icons,
        'child_icons': child_icons,
        'adult_count': adult_count,
        'child_count': child_count,
        'price': 'EUR 26',
        'additional_tax': 'Градска такса',
        'tax': '',
        'tax': 'BGN 0.8',
        'total': 'EUR 26',
        "star_range": range((int(hotel_rating)))
    }
    return render(request, 'myapp/base.html', context)
