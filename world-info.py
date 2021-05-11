import io
import requests
import tkinter as tk
import multiprocessing
import time
import tzwhere
import geopy
import datetime
import pytz
from pytz import timezone
from os import name
from typing import Text
from tqdm import tqdm
from datetime import date
from bs4 import BeautifulSoup
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy import distance
from geopy import timezone
from tkinter import PhotoImage, constants
from urllib.request import urlopen, Request
from tkinter.constants import CENTER, LEFT, RIGHT, SEPARATOR, SUNKEN


def empty():
    return


try:
    def show_covid():
        global active_covid
        global covid_container
        global covid_total_image
        global covid_recovered_image
        global covid_total_cases_num
        global covid_recovered_cases_num
        global covid_fatal_cases_num
        global new_covid_fatal_cases_num
        global new_covid_recovered_cases_num
        global new_covid_total_cases_num
        global per_country_search

        try:
            weather_container.place_forget()
            active_weather.place_forget()
            weather.configure(command=show_weather)
        except Exception as e:
            print(e)

        try:
            active_global.place_forget()
            global_time.configure(command=show_global)
            global_container.place_forget()
        except Exception as e:
            print(e)

        try:
            settings_container.place_forget()
            settings.configure(command=show_settings)
            active_settings.place_forget()
        except Exception as e:
            print(e)

        try:
            active_covid = tk.Frame(top_menu, bg=bar)
            active_covid.place(relwidth=0.141, relheight=0.07,
                               relx=0, rely=0.97)
        except Exception as e:
            print(e)

        try:
            covid.configure(command=empty)
        except Exception as e:
            print(e)

        covid_container = tk.Frame(root, bg=bg)
        covid_container.place(relwidth=0.97, relheight=0.785,
                              rely=0.195, relx=0.015)

        covid_total_cases = tk.Label(covid_container, bg=bg, fg=txt,
                                     width=18, height=1, anchor=tk.CENTER, font=font_2, text="Total Cases")
        covid_total_cases.grid(row=0, column=0, padx=20, pady=(100, 20))

        covid_total_cases_num = tk.Label(
            covid_container, bg=bg, fg=txt, width=18, height=1, anchor=tk.CENTER, font=font_2, text="-")
        covid_total_cases_num.grid(row=1, column=0)

        new_covid_total_cases = tk.Label(covid_container, bg=bg, fg=txt,
                                         width=18, height=1, anchor=tk.CENTER, font=font_2, text="New Cases")
        new_covid_total_cases.grid(row=2, column=0, padx=20, pady=(90, 20))

        new_covid_total_cases_num = tk.Label(
            covid_container, bg=bg, fg=txt, width=18, height=1, anchor=tk.CENTER, font=font_2, text="-")
        new_covid_total_cases_num.grid(row=3, column=0)

        frame_separator = tk.Frame(covid_container, bg=txt)
        frame_separator.place(
            relwidth=0.002, relheight=0.65, relx=0.33, rely=0.2)

        covid_recovered_cases = tk.Label(covid_container, bg=bg, fg=txt,
                                         width=18, height=1, anchor=tk.CENTER, font=font_2, text="Recovered")
        covid_recovered_cases.grid(
            row=0, column=1, padx=20, pady=(100, 20))

        covid_recovered_cases_num = tk.Label(
            covid_container, bg=bg, fg=txt, width=18, height=1, anchor=tk.CENTER, font=font_2, text="-")
        covid_recovered_cases_num.grid(row=1, column=1)

        new_covid_recovered_cases = tk.Label(covid_container, bg=bg, fg=txt,
                                             width=18, height=1, anchor=tk.CENTER, font=font_2, text="New Recovered")
        new_covid_recovered_cases.grid(
            row=2, column=1, padx=20, pady=(90, 20))

        new_covid_recovered_cases_num = tk.Label(
            covid_container, bg=bg, fg=txt, width=18, height=1, anchor=tk.CENTER, font=font_2, text="-")
        new_covid_recovered_cases_num.grid(row=3, column=1)

        frame_separator_2 = tk.Frame(covid_container, bg=txt)
        frame_separator_2.place(
            relwidth=0.002, relheight=0.65, relx=0.64, rely=0.2)

        covid_fatal_cases = tk.Label(covid_container, bg=bg, fg=txt,
                                     width=18, height=1, anchor=tk.CENTER, font=font_2, text="Deaths")
        covid_fatal_cases.grid(row=0, column=2, padx=20, pady=(100, 20))

        covid_fatal_cases_num = tk.Label(
            covid_container, bg=bg, fg=txt, width=18, height=1, anchor=tk.CENTER, font=font_2, text="-")
        covid_fatal_cases_num.grid(row=1, column=2)

        new_covid_fatal_cases = tk.Label(covid_container, bg=bg, fg=txt,
                                         width=18, height=1, anchor=tk.CENTER, font=font_2, text="New Deaths")
        new_covid_fatal_cases.grid(row=2, column=2, padx=20, pady=(90, 20))

        new_covid_fatal_cases_num = tk.Label(
            covid_container, bg=bg, fg=txt, width=18, height=1, anchor=tk.CENTER, font=font_2, text="-")
        new_covid_fatal_cases_num.grid(row=3, column=2)

        per_country_search_frame = tk.Frame(covid_container, bg=bg_2)
        per_country_search_frame.place(
            relwidth=0.82, relheight=0.1, relx=0.085, rely=0.03)

        def enter(event):
            per_country_search.configure(fg=txt)
            per_country_search.delete(0, 'end')

        def leave(event):
            per_country_search.configure(fg="#4d4d4d")
            per_country_search.insert(0, 'ex. Croatia, Germany, World')

        per_country_search = tk.Entry(per_country_search_frame, bg=bg_2, fg="#4d4d4d", bd=0, font=(
            "Oxygen", 14), width=100, textvariable=1, justify='left')
        per_country_search.delete(0, 'end')
        per_country_search.insert(
            0, 'ex. Croatia, Germany, World')
        per_country_search.bind("<FocusIn>", enter)
        per_country_search.bind("<FocusOut>", leave)
        per_country_search.bind("<Return>", country_covid)
        per_country_search.pack(padx=10, ipady=10)

        check_time()
        root.after(100, get_covid_data)
except Exception as e:
    f = open("error.txt", "a")
    f.write(f"Error: {e}\n")
    f.close()

try:
    def get_covid_data():

        def total_data():
            url = "https://www.worldometers.info/coronavirus"
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

            web_byte = urlopen(req).read()

            bs = BeautifulSoup(web_byte, "html.parser")

            items = bs.findAll(id="maincounter-wrap")

            items_list = []

            with io.open('E:\Total_Cases.txt', 'w', encoding='utf-8') as web:
                web.write(str(items))
            with io.open('E:\Total_Cases.txt', 'r', encoding='utf-8') as nums:
                for line in nums:
                    for word in line.split():
                        if "</span>" in word:
                            items_list.append(line)

            total = ""
            recov = ""
            death = ""

            for i in items_list[0]:
                if i.isdigit() or i == ",":
                    total += i

            for i in items_list[1]:
                if i.isdigit() or i == ",":
                    death += i

            for i in items_list[2]:
                if i.isdigit() or i == ",":
                    recov += i

            covid_total_cases_num.configure(text=f"{total}")
            covid_recovered_cases_num.configure(text=f"{recov}")
            covid_fatal_cases_num.configure(text=f"{death}")

        def new_data():
            url = "https://www.worldometers.info/coronavirus"
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

            web_byte = urlopen(req).read()

            bs = BeautifulSoup(web_byte, "html.parser")

            items = bs.find('td', text='World').parent.find_all('td')

            new_cases_list = []

            with io.open('E:\casesToday.txt', 'w', encoding='utf-8') as web:
                web.write(str(items))
            with io.open('E:\casesToday.txt', 'r', encoding='utf-8') as nums:
                for line in nums:
                    for word in line.split():
                        if "+" in word:
                            new_cases_list.append(word)

            total_new = ""
            death_new = ""
            recov_new = ""

            for i in new_cases_list[0]:
                if i.isdigit() or i == ",":
                    total_new += i

                if i == "/":
                    break

            for i in new_cases_list[1]:
                if i.isdigit() or i == ",":
                    death_new += i

                if i == "/":
                    break

            for i in new_cases_list[2]:
                if i.isdigit() or i == ",":
                    recov_new += i

                if i == "/":
                    break

            new_covid_total_cases_num.configure(text=f"+{total_new}")
            new_covid_fatal_cases_num.configure(text=f"+{death_new}")
            new_covid_recovered_cases_num.configure(text=f"+{recov_new}")

        total_data()
        new_data()

except Exception as e:
    f = open("error.txt", "a")
    f.write(f"Error: {e}\n")
    f.close()


try:
    def country_covid(event):
        global country_name
        country_name = per_country_search.get()

        if country_name.lower() != "world":

            try:
                def country_total():
                    country_name = per_country_search.get()

                    country_name_new = ""

                    for i in country_name:
                        if i == " ":
                            country_name_new += "-"
                        else:
                            country_name_new += i

                    if country_name_new.lower() == "usa" or country_name_new.lower() == "america" or country_name_new.lower() == "north america" or country_name_new.lower() == "us":
                        country_name_new = "us"

                    if country_name_new.lower() == "united kingdom" or country_name_new.lower() == "great britain" or country_name_new.lower() == "britain" or country_name_new.lower() == "uk":
                        country_name_new = "uk"

                    url = f"https://www.worldometers.info/coronavirus/country/{country_name_new.lower()}"

                    req = Request(
                        url, headers={'User-Agent': 'Mozilla/5.0'})

                    web_byte = urlopen(req).read()

                    bs = BeautifulSoup(web_byte, "html.parser")

                    items = bs.findAll(id="maincounter-wrap")

                    per_country_list = []

                    with io.open('E:\Per_Country_Cases.txt', 'w', encoding='utf-8') as web:
                        web.write(str(items))
                    with io.open('E:\Per_Country_Cases.txt', 'r', encoding='utf-8') as nums:
                        for line in nums:
                            for word in line.split():
                                if "</span>" in word:
                                    per_country_list.append(line)

                    total_country = ""
                    recov_country = ""
                    death_country = ""

                    for i in per_country_list[0]:
                        if i.isdigit() or i == ",":
                            total_country += i

                    for i in per_country_list[1]:
                        if i.isdigit() or i == ",":
                            death_country += i

                    for i in per_country_list[2]:
                        if i.isdigit() or i == ",":
                            recov_country += i

                    covid_total_cases_num.configure(
                        text=f"{total_country}")
                    covid_recovered_cases_num.configure(
                        text=f"{recov_country}")
                    covid_fatal_cases_num.configure(
                        text=f"{death_country}")

            except Exception as e:
                print(e)

            try:
                def country_new():
                    country_name = per_country_search.get()

                    if country_name.lower() == "usa" or country_name.lower() == "america" or country_name.lower() == "north america" or country_name.lower() == "us":
                        country_name = "USA"

                    elif country_name.lower() == "united kingdom" or country_name.lower() == "great britain" or country_name.lower() == "britain" or country_name.lower() == "uk":
                        country_name = "UK"

                    url = "https://www.worldometers.info/coronavirus"
                    req = Request(
                        url, headers={'User-Agent': 'Mozilla/5.0'})

                    web_byte = urlopen(req).read()

                    bs = BeautifulSoup(web_byte, "html.parser")

                    if str(country_name) == "USA" or str(country_name) == "UK":
                        country_items = bs.find(
                            'td', text=f'{country_name}').parent.find_all('td')
                    else:
                        country_items = bs.find(
                            'td', text=f'{country_name.title()}').parent.find_all('td')

                    new_cases_country = []

                    with io.open('E:\casesCountry.txt', 'w', encoding='utf-8') as web:
                        web.write(str(country_items))
                    with io.open('E:\casesCountry.txt', 'r', encoding='utf-8') as nums:
                        for line in nums:
                            for word in line.split():
                                if "+" in word:
                                    new_cases_country.append(word)

                    total_new_country = ""
                    death_new_country = ""
                    recov_new_country = ""

                    try:
                        for i in new_cases_country[0]:
                            if i.isdigit() or i == ",":
                                total_new_country += i

                            if i == "/":
                                break

                        if total_new_country.startswith("000"):
                            new_covid_total_cases_num.configure(
                                text=f"+{total_new_country[3:]}")
                        else:
                            new_covid_total_cases_num.configure(
                                text=f"+{total_new_country}")

                    except:
                        new_covid_total_cases_num.configure(
                            text=f"+0")

                    try:
                        for i in new_cases_country[1]:
                            if i.isdigit() or i == ",":
                                death_new_country += i

                            if i == "/":
                                break
                        if death_new_country.startswith("000"):
                            new_covid_fatal_cases_num.configure(
                                text=f"+{death_new_country[3:]}")
                        else:
                            new_covid_fatal_cases_num.configure(
                                text=f"+{death_new_country}")

                    except:
                        new_covid_fatal_cases_num.configure(
                            text=f"+0")

                    try:
                        for i in new_cases_country[2]:
                            if i.isdigit() or i == ",":
                                recov_new_country += i

                            if i == "/":
                                break
                        if recov_new_country.startswith("000"):
                            new_covid_recovered_cases_num.configure(
                                text=f"+{recov_new_country[3:]}")
                        else:
                            new_covid_recovered_cases_num.configure(
                                text=f"+{recov_new_country}")

                    except:
                        new_covid_recovered_cases_num.configure(
                            text=f"+0")
            except Exception as e:
                print(e)

            country_total()
            country_new()
        else:
            get_covid_data()

except Exception as e:
    f = open("error.txt", "a")
    f.write(f"Error: {e}\n")
    f.close()


def check_time():

    time_frame = tk.Frame(covid_container, bg=bg)
    time_frame.place(relwidth=0.25, relheight=0.2, relx=0.76, rely=0.95)

    datetime_label = tk.Label(time_frame, bg=bg, fg=txt, width=8, height=1, font=(
        "Oxygen", 11), anchor=tk.W, text=f"Datetime:")
    datetime_label.grid(row=0, column=0, padx=0, pady=0)

    def times():
        global time_ref
        time_and_date = datetime.now()

        only_time = time_and_date.strftime("%H:%M:%S")

        only_date = time_and_date.strftime("%d/%m/%Y")

        time_label = tk.Label(time_frame, bg=bg, fg=txt, width=20, height=1, font=(
            "Oxygen", 11), anchor=tk.W, text=f"{only_date} • {only_time}")
        time_label.grid(row=0, column=1, padx=(0, 2), pady=0)

        time_ref = root.after(1000, times)

    times()


def show_weather():
    global per_city_weather
    global active_weather
    global weather_container
    global cloudy
    global partly_cloudy
    global drizzle
    global storm
    global snowy
    global sunny
    global rainy
    global foggy
    global temp_min
    global temp_max
    global temp_now
    global weather_condition
    global weather_icon
    global pressure_info
    global humidity_info
    global wind_info
    global sunset_info
    global sunrise_info
    global now_showing_text
    global cloudiness
    global few_clouds
    global scattered_clouds
    global broken_clouds
    global overcast_clouds
    global clear_weather
    global drizzle_new
    global foggy_new
    global rainy_new
    global snowy_new
    global light_storm
    global heavy_storm_no_rain
    global storm_with_rain

    try:
        root.after_cancel(time_ref)
        covid_container.place_forget()
        active_covid.place_forget()
        covid.configure(command=show_covid)
    except Exception as e:
        print(e)

    try:
        global_container.place_forget()
        active_global.place_forget()
        global_time.configure(command=show_global)
    except Exception as e:
        print(e)

    try:
        settings_container.place_forget()
        settings.configure(command=show_settings)
        active_settings.place_forget()
    except Exception as e:
        print(e)

    try:

        active_weather = tk.Frame(top_menu, bg=bar)
        active_weather.place(relwidth=0.141, relheight=0.07,
                             relx=0.141, rely=0.97)
    except Exception as e:
        print(e)

    try:
        weather.configure(command=empty)
    except Exception as e:
        print(e)

    # Weather icons for different weather conditions
    # Old icons
    """
    cloudy = PhotoImage(file="images/cloudy.png")
    partly_cloudy = PhotoImage(file="images/partly_cloudy.png")
    rainy = PhotoImage(file="images/rainy.png")
    snowy = PhotoImage(file="images/snowy.png")
    storm = PhotoImage(file="images/storm.png")
    sunny = PhotoImage(file="images/sunny.png")
    drizzle = PhotoImage(file="images/drizzle.png")
    foggy = PhotoImage(file="images/fog.png")
    """

    # New icons

    # Cloudy
    few_clouds = PhotoImage(file="images/Clouds/few_clouds.png")
    scattered_clouds = PhotoImage(file="images/Clouds/scattered_clouds.png")
    broken_clouds = PhotoImage(file="images/Clouds/broken_clouds.png")
    overcast_clouds = PhotoImage(file="images/Clouds/overcast_clouds.png")

    # Clear
    clear_weather = PhotoImage(file="images/Clear/sunny.png")

    # Drizzle
    drizzle_new = PhotoImage(file="images/Drizzle/drizzle.png")

    # Fog
    foggy_new = PhotoImage(file="images/Fog/fog.png")

    # Rain
    rainy_new = PhotoImage(file="images/Rain/rainy.png")

    # Snow
    snowy_new = PhotoImage(file="images/Snowy/snow.png")

    # Thunderstorm
    light_storm = PhotoImage(file="images/Thunderstorm/light_storm.png")
    heavy_storm_no_rain = PhotoImage(
        file="images/Thunderstorm/heavy_storm_no_rain.png")
    storm_with_rain = PhotoImage(
        file="images/Thunderstorm/storm_with_rain.png")

    weather_container = tk.Frame(root, bg=bg)
    weather_container.place(
        relwidth=0.97, relheight=0.785, rely=0.195, relx=0.015)

    per_city_weather_frame = tk.Frame(weather_container, bg=bg_2)
    per_city_weather_frame.place(
        relwidth=0.82, relheight=0.1, relx=0.085, rely=0.03)

    def enter(event):
        per_city_weather.configure(fg=txt)
        per_city_weather.delete(0, 'end')

    def leave(event):
        per_city_weather.configure(fg="#4d4d4d")
        per_city_weather.insert(0, 'ex. Washington, London, Zagreb')

    per_city_weather = tk.Entry(per_city_weather_frame, bg=bg_2, fg="#4d4d4d", bd=0, font=(
        "Oxygen", 14), width=100, textvariable=1, justify='left')
    per_city_weather.delete(0, 'end')
    per_city_weather.insert(
        0, 'ex. Washington, London, Zagreb')
    per_city_weather.bind("<FocusIn>", enter)
    per_city_weather.bind("<FocusOut>", leave)
    per_city_weather.bind("<Return>", get_weather)
    per_city_weather.pack(padx=10, ipady=10)

    now_showing_frame = tk.Frame(weather_container, bg=bg)
    now_showing_frame.place(relwidth=0.7, relheight=0.12, relx=0.15, rely=0.16)

    now_showing_text = tk.Label(now_showing_frame, bg=bg, fg="white", anchor=tk.CENTER,
                                width=100, height=1, font=("Oxygen", 20), text="Country, Country Code")
    now_showing_text.pack()

    weather_icon_frame = tk.Frame(weather_container, bg=bg)
    weather_icon_frame.place(
        relwidth=0.1, relheight=0.20, relx=0.22, rely=0.34)

    weather_icon = tk.Button(weather_icon_frame, bg=bg,
                             width=72, height=72, image=few_clouds, relief=SUNKEN, activebackground=bg, activeforeground=txt, bd=0)
    weather_icon.pack()

    weather_condition_frame = tk.Frame(weather_container, bg=bg)
    weather_condition_frame.place(
        relwidth=0.4, relheight=0.15, relx=0.068, rely=0.51)

    weather_condition = tk.Label(weather_condition_frame, bg=bg, fg="white", width=20,
                                 height=1, anchor=tk.CENTER, font=("Oxygen", 25), text="Partly Cloudy")
    weather_condition.pack()

    temp_container = tk.Frame(weather_container, bg=bg)
    temp_container.place(relwidth=0.50, relheight=0.20, relx=0.093, rely=0.64)

    temp_min = tk.Label(temp_container, bg=bg, fg="white", width=7, height=1, font=(
        "Oxygen", 14), anchor=tk.CENTER, text="Min: 6°C")
    temp_min.grid(row=0, column=0, padx=15, pady=0)

    temp_now = tk.Label(temp_container, bg=bg, fg="white", width=4, height=1, font=(
        "Oxygen", 37), anchor=tk.CENTER, text="12°C")
    temp_now.grid(row=0, column=1, padx=0, pady=0)

    temp_max = tk.Label(temp_container, bg=bg, fg="white", width=10, height=1, font=(
        "Oxygen", 14), anchor=tk.CENTER, text="Max: 21°C")
    temp_max.grid(row=0, column=2, padx=0, pady=0)

    line_separator = tk.Frame(weather_container, bg="white")
    line_separator.place(relwidth=0.003, relheight=0.5, relx=0.5, rely=0.3)

    additional_info_container = tk.Frame(weather_container, bg=bg)
    additional_info_container.place(
        relwidth=0.3, relheight=0.52, relx=0.57, rely=0.328)

    pressure_info = tk.Label(additional_info_container, bg=bg, fg="white", anchor=tk.W,
                             width=100, height=1, font=("Oxygen", 17), text="Pressure: 1000 HPa")
    pressure_info.grid(row=0, column=0, padx=0, pady=0)

    humidity_info = tk.Label(additional_info_container, bg=bg, fg="white", anchor=tk.W,
                             width=100, height=1, font=("Oxygen", 17), text="Humidity: 100%")
    humidity_info.grid(row=1, column=0, padx=0, pady=0)

    wind_info = tk.Label(additional_info_container, bg=bg, fg="white", anchor=tk.W,
                         width=100, height=1, font=("Oxygen", 17), text="Wind: 100 KM/h")
    wind_info.grid(row=2, column=0, padx=0, pady=0)

    cloudiness = tk.Label(additional_info_container, bg=bg, fg="white", anchor=tk.W,
                          width=100, height=1, font=("Oxygen", 17), text="Clouds: 100%")
    cloudiness.grid(row=3, column=0, padx=0, pady=0)

    sunset_info = tk.Label(additional_info_container, bg=bg, fg="white", anchor=tk.W,
                           width=100, height=1, font=("Oxygen", 17), text="Sunset: 09:00 PM")
    sunset_info.grid(row=4, column=0, padx=0, pady=0)

    sunrise_info = tk.Label(additional_info_container, bg=bg, fg="white", anchor=tk.W,
                            width=100, height=1, font=("Oxygen", 17), text="Sunrise: 06:00 AM")
    sunrise_info.grid(row=5, column=0, padx=0, pady=0)

    root.after(100, get_weather_default)


def get_weather(event):

    try:
        if not per_city_weather.get():
            city = "bjelovar"
        else:
            city = per_city_weather.get()

        #g = Nominatim(user_agent='world-info').geocode(city.title())

        #tmz = timezone()

        # print(tmz)

        api = "http://api.openweathermap.org/data/2.5/weather?q=" + \
            city.lower() + "&units=metric" + "&appid=c72495374f5e753c25a030e6d5b114f1"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        condition_extended = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'])
        min_temp = int(json_data['main']['temp_min'])
        max_temp = int(json_data['main']['temp_max'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = float(json_data['wind']['speed'] * 3.6)
        wind_direction = json_data['wind']['deg']
        cloudiness_value = json_data['clouds']['all']
        sunrise = time.strftime("%I:%M", time.localtime(
            json_data['sys']['sunrise']))
        sunset = time.strftime("%I:%M", time.localtime(
            json_data['sys']['sunset']))
        city_code = json_data['sys']['country']

        wind_direc_compass = ""

        # Wind direction conversion from degrees to abbrevation
        if float(wind_direction) >= 0 and float(wind_direction) < 22.5:
            wind_direc_compass = "N"
        elif float(wind_direction) >= 22.5 and float(wind_direction) < 45:
            wind_direc_compass = "NNE"
        elif float(wind_direction) >= 45 and float(wind_direction) < 67.5:
            wind_direc_compass = "NE"
        elif float(wind_direction) >= 67.5 and float(wind_direction) < 90:
            wind_direc_compass = "ENE"
        elif float(wind_direction) >= 90 and float(wind_direction) < 112.5:
            wind_direc_compass = "E"
        elif float(wind_direction) >= 112.5 and float(wind_direction) < 135:
            wind_direc_compass = "ESE"
        elif float(wind_direction) >= 135 and float(wind_direction) < 157.5:
            wind_direc_compass = "SE"
        elif float(wind_direction) >= 157.5 and float(wind_direction) < 180:
            wind_direc_compass = "SSE"
        elif float(wind_direction) >= 180 and float(wind_direction) < 202.5:
            wind_direc_compass = "S"
        elif float(wind_direction) >= 202.5 and float(wind_direction) < 225:
            wind_direc_compass = "SSW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 247.5:
            wind_direc_compass = "SW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 270:
            wind_direc_compass = "WSW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 292.5:
            wind_direc_compass = "W"
        elif float(wind_direction) >= 225 and float(wind_direction) < 315:
            wind_direc_compass = "WNW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 337:
            wind_direc_compass = "NW"
        else:
            wind_direc_compass = "NNW"

        thunderstorm_with_rain = ["thunderstorm with light rain", "thunderstorm with rain", "thunderstorm with heavy rain",
                                  "thunderstorm with light drizzle", "thunderstorm with drizzle", "thunderstorm with heavy drizzle"]
        thunderstorm_no_rain = ["light thunderstorm", "thunderstorm"]
        heavy_thunderstorm = ["heavy thunderstorm", "ragged thunderstorm"]

        if condition.lower() == "clear":
            weather_icon.configure(image=clear_weather)
        elif condition.lower() == "rain":
            weather_icon.configure(image=rainy_new)
        elif condition.lower() == "thunderstorm":
            if thunderstorm_with_rain in condition_extended.lower():
                weather_icon.configure(image=light_storm)
            elif thunderstorm_no_rain in condition_extended.lower():
                weather_icon.configure(image=storm_with_rain)
            elif heavy_thunderstorm in condition_extended.lower():
                weather_icon.configure(image=heavy_storm_no_rain)
        elif condition.lower() == "clouds":
            if condition_extended.lower() == "few clouds":
                weather_icon.configure(image=few_clouds)
            elif condition_extended.lower() == "scattered clouds":
                weather_icon.configure(image=scattered_clouds)
            elif condition_extended.lower() == "broken clouds":
                weather_icon.configure(image=broken_clouds)
            elif condition_extended.lower() == "overcast clouds":
                weather_icon.configure(image=overcast_clouds)
        elif condition.lower() == "drizzle":
            weather_icon.configure(image=drizzle_new)
        elif condition.lower() == "snow":
            weather_icon.configure(image=snowy_new)
        elif condition_extended.lower() == "mist" or condition_extended.lower() == "smoke" or condition_extended.lower() == "haze" or condition_extended.lower() == "dust" or condition_extended.lower() == "fog" or condition_extended.lower() == "sand/ dust whirls" or condition_extended.lower() == "dust" or condition_extended.lower() == "volcanic ash" or condition_extended.lower() == "squalls" or condition_extended.lower() == "tornado":
            weather_icon.configure(image=foggy_new)

        now_showing_text.configure(text=f"{city.title()}, {city_code}")
        weather_condition.configure(text=f"{condition_extended.title()}")
        temp_now.configure(text=f"{temp}°C")
        temp_min.configure(text=f"Min: {min_temp}°C")
        temp_max.configure(text=f"Max: {max_temp}°C")
        pressure_info.configure(text=f"Pressure: {pressure} HPa")
        humidity_info.configure(text=f"Humidity: {humidity}%")
        wind_info.configure(
            text=f"Wind: {wind_direc_compass} {wind:.1f} km/hr")
        cloudiness.configure(text=f"Clouds: {cloudiness_value}%")
        sunrise_info.configure(text=f"Sunrise: {sunrise} AM")
        sunset_info.configure(text=f"Sunset: {sunset} PM")
    except Exception as e:
        print(e)


def get_weather_default():

    try:
        city = "Bjelovar"

        api = "http://api.openweathermap.org/data/2.5/weather?q=" + \
            city.lower() + "&units=metric" + "&appid=c72495374f5e753c25a030e6d5b114f1"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        condition_extended = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'])
        min_temp = int(json_data['main']['temp_min'])
        max_temp = int(json_data['main']['temp_max'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = float(json_data['wind']['speed'] * 3.6)
        wind_direction = json_data['wind']['deg']
        cloudiness_value = json_data['clouds']['all']
        sunrise = time.strftime("%I:%M", time.gmtime(
            json_data['sys']['sunrise'] + 7200))
        sunset = time.strftime("%I:%M", time.gmtime(
            json_data['sys']['sunset'] + 7200))
        city_code = json_data['sys']['country']

        wind_direc_compass = ""

        # Wind direction conversion from degrees to abbrevation
        if float(wind_direction) >= 0 and float(wind_direction) < 22.5:
            wind_direc_compass = "N"
        elif float(wind_direction) >= 22.5 and float(wind_direction) < 45:
            wind_direc_compass = "NNE"
        elif float(wind_direction) >= 45 and float(wind_direction) < 67.5:
            wind_direc_compass = "NE"
        elif float(wind_direction) >= 67.5 and float(wind_direction) < 90:
            wind_direc_compass = "ENE"
        elif float(wind_direction) >= 90 and float(wind_direction) < 112.5:
            wind_direc_compass = "E"
        elif float(wind_direction) >= 112.5 and float(wind_direction) < 135:
            wind_direc_compass = "ESE"
        elif float(wind_direction) >= 135 and float(wind_direction) < 157.5:
            wind_direc_compass = "SE"
        elif float(wind_direction) >= 157.5 and float(wind_direction) < 180:
            wind_direc_compass = "SSE"
        elif float(wind_direction) >= 180 and float(wind_direction) < 202.5:
            wind_direc_compass = "S"
        elif float(wind_direction) >= 202.5 and float(wind_direction) < 225:
            wind_direc_compass = "SSW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 247.5:
            wind_direc_compass = "SW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 270:
            wind_direc_compass = "WSW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 292.5:
            wind_direc_compass = "W"
        elif float(wind_direction) >= 225 and float(wind_direction) < 315:
            wind_direc_compass = "WNW"
        elif float(wind_direction) >= 225 and float(wind_direction) < 337:
            wind_direc_compass = "NW"
        else:
            wind_direc_compass = "NNW"

        thunderstorm_with_rain = ["thunderstorm with light rain", "thunderstorm with rain", "thunderstorm with heavy rain",
                                  "thunderstorm with light drizzle", "thunderstorm with drizzle", "thunderstorm with heavy drizzle"]
        thunderstorm_no_rain = ["light thunderstorm", "thunderstorm"]
        heavy_thunderstorm = ["heavy thunderstorm", "ragged thunderstorm"]

        if condition.lower() == "clear":
            weather_icon.configure(image=clear_weather)
        elif condition.lower() == "rain":
            weather_icon.configure(image=rainy_new)
        elif condition.lower() == "thunderstorm":
            if thunderstorm_with_rain in condition_extended.lower():
                weather_icon.configure(image=light_storm)
            elif thunderstorm_no_rain in condition_extended.lower():
                weather_icon.configure(image=storm_with_rain)
            elif heavy_thunderstorm in condition_extended.lower():
                weather_icon.configure(image=heavy_storm_no_rain)
        elif condition.lower() == "clouds":
            if condition_extended.lower() == "few clouds":
                weather_icon.configure(image=few_clouds)
            elif condition_extended.lower() == "scattered clouds":
                weather_icon.configure(image=scattered_clouds)
            elif condition_extended.lower() == "broken clouds":
                weather_icon.configure(image=broken_clouds)
            elif condition_extended.lower() == "overcast clouds":
                weather_icon.configure(image=overcast_clouds)
        elif condition.lower() == "drizzle":
            weather_icon.configure(image=drizzle_new)
        elif condition.lower() == "snow":
            weather_icon.configure(image=snowy_new)
        elif condition_extended.lower() == "mist" or condition_extended.lower() == "smoke" or condition_extended.lower() == "haze" or condition_extended.lower() == "dust" or condition_extended.lower() == "fog" or condition_extended.lower() == "sand/ dust whirls" or condition_extended.lower() == "dust" or condition_extended.lower() == "volcanic ash" or condition_extended.lower() == "squalls" or condition_extended.lower() == "tornado":
            weather_icon.configure(image=foggy_new)

        now_showing_text.configure(text=f"{city.title()}, {city_code}")
        weather_condition.configure(text=f"{condition_extended.title()}")
        temp_now.configure(text=f"{temp}°C")
        temp_min.configure(text=f"Min: {min_temp}°C")
        temp_max.configure(text=f"Max: {max_temp}°C")
        pressure_info.configure(text=f"Pressure: {pressure} HPa")
        humidity_info.configure(text=f"Humidity: {humidity}%")
        wind_info.configure(
            text=f"Wind: {wind_direc_compass} {wind:.1f} km/hr")
        cloudiness.configure(text=f"Clouds: {cloudiness_value}%")
        sunrise_info.configure(text=f"Sunrise: {sunrise} AM")
        sunset_info.configure(text=f"Sunset: {sunset} PM")
    except Exception as e:
        print(e)


def show_global():
    global active_global
    global global_container
    global cest_time_clock
    global gmt_clock
    global utc_clock
    global pst_clock

    try:
        covid_container.place_forget()
        active_covid.place_forget()
        covid.configure(command=show_covid)
    except Exception as e:
        print(e)

    try:
        weather_container.place_forget()
        active_weather.place_forget()
        weather.configure(command=show_weather)
    except Exception as e:
        print(e)

    try:
        settings_container.place_forget()
        settings.configure(command=show_settings)
        active_settings.place_forget()
    except Exception as e:
        print(e)

    try:
        active_global = tk.Frame(top_menu, bg=bar)
        active_global.place(relwidth=0.141, relheight=0.07,
                            relx=0.282, rely=0.97)

        global_time.configure(command=empty)
    except Exception as e:
        print(e)

    global_container = tk.Frame(root, bg=bg)
    global_container.place(
        relwidth=0.97, relheight=0.785, rely=0.195, relx=0.015)

    cest_time_frame = tk.Frame(global_container, bg=bg)
    cest_time_frame.place(relwidth=0.4, relheight=0.4, relx=0.09, rely=0.1)

    cest_time_clock = tk.Label(cest_time_frame, bg=bg, fg="white", width=10,
                               height=1, anchor=tk.CENTER, font=("Oxygen", 35), text="16:00")
    cest_time_clock.grid(row=0, column=0, padx=0, pady=7)

    cest_time_name = tk.Label(cest_time_frame, bg=bg, fg="white", width=28,
                              height=2, anchor=tk.CENTER, font=("Oxygen", 15), text="Central European Summer Time\n(CEST)")
    cest_time_name.grid(row=1, column=0, padx=0, pady=0)

    utc_frame = tk.Frame(global_container, bg=bg)
    utc_frame.place(relwidth=0.4, relheight=0.4, relx=0.57, rely=0.1)

    utc_clock = tk.Label(utc_frame, bg=bg, fg="white", width=10,
                         height=1, anchor=tk.CENTER, font=("Oxygen", 35), text="16:00")
    utc_clock.grid(row=0, column=0, padx=0, pady=7)

    utc_name = tk.Label(utc_frame, bg=bg, fg="white", width=28,
                        height=2, anchor=tk.CENTER, font=("Oxygen", 15), text="Coordinated Universal Time\n(UTC)")
    utc_name.grid(row=1, column=0, padx=0, pady=0)

    gmt_frame = tk.Frame(global_container, bg=bg)
    gmt_frame.place(relwidth=0.4, relheight=0.4, relx=0.09, rely=0.58)

    gmt_clock = tk.Label(gmt_frame, bg=bg, fg="white", width=10,
                         height=1, anchor=tk.CENTER, font=("Oxygen", 35), text="16:00")
    gmt_clock.grid(row=0, column=0, padx=0, pady=7)

    gmt_name = tk.Label(gmt_frame, bg=bg, fg="white", width=28,
                        height=2, anchor=tk.CENTER, font=("Oxygen", 15), text="Greenwich Mean Time\n(GMT)")
    gmt_name.grid(row=1, column=0, padx=0, pady=0)

    pst_frame = tk.Frame(global_container, bg=bg)
    pst_frame.place(relwidth=0.4, relheight=0.4, relx=0.57, rely=0.58)

    pst_clock = tk.Label(pst_frame, bg=bg, fg="white", width=10,
                         height=1, anchor=tk.CENTER, font=("Oxygen", 35), text="16:00")
    pst_clock.grid(row=0, column=0, padx=0, pady=7)

    pst_name = tk.Label(pst_frame, bg=bg, fg="white", width=28,
                        height=2, anchor=tk.CENTER, font=("Oxygen", 15), text="Pacific Standard Time\n(PST)")
    pst_name.grid(row=1, column=0, padx=0, pady=0)

    get_global_time()


def get_global_time():

    utc_now = datetime.utcnow().strftime("%H:%M")

    gmt_now = datetime.now().strftime("%H:%M")

    pst = pytz.timezone('America/Los_Angeles')

    pst_now = datetime.now(pst).strftime("%H:%M")

    cest = pytz.timezone('Europe/Paris')

    cest_now = datetime.now(cest).strftime("%H:%M")

    cest_time_clock.configure(text=f"{cest_now}")

    gmt_clock.configure(text=f"{gmt_now}")

    pst_clock.configure(text=f"{pst_now}")

    utc_clock.configure(text=f"{utc_now}")

    root.after(1000, get_global_time)


def show_settings():
    global settings_container
    global active_settings
    global on_button
    global off_button

    try:
        covid_container.place_forget()
        active_covid.place_forget()
        covid.configure(command=show_covid)
    except Exception as e:
        print(e)

    try:
        weather_container.place_forget()
        active_weather.place_forget()
        weather.configure(command=show_weather)
    except Exception as e:
        print(e)

    try:
        global_container.place_forget()
        active_global.place_forget()
        global_time.configure(command=show_global)
    except Exception as e:
        print(e)

    try:
        active_settings = tk.Frame(top_menu, bg=bar)
        active_settings.place(relwidth=0.141, relheight=0.07,
                              relx=0.423, rely=0.97)

        settings.configure(command=empty)
    except Exception as e:
        print(e)

    """
    settings_container = tk.Frame(root, bg=bg)
    settings_container.place(
        relwidth=0.97, relheight=0.785, rely=0.195, relx=0.015)

    covid_settings_frame = tk.Frame(settings_container, bg=bg)
    covid_settings_frame.place(
        relwidth=0.37, relheight=0.8, relx=0.02, rely=0.06)

    covid_settings_title_frame = tk.Frame(covid_settings_frame, bg=bg)
    covid_settings_title_frame.place(
        relwidth=1, relheight=0.12, relx=0, rely=0)

    covid_settings_title = tk.Label(covid_settings_title_frame, bg=bg, fg="white", width=30, height=1, font=(
        "Oxygen", 18), anchor=tk.W, text="COVID-19")
    covid_settings_title.pack()

    covid_settings_separator = tk.Frame(covid_settings_title_frame, bg="white")
    covid_settings_separator.place(
        relwidth=1, relheight=0.004, relx=0, rely=0.9)

    on_button = PhotoImage(file="images/Switches/switch-on_small.png")
    off_button = PhotoImage(file="images/Switches/switch-off_small.png")
    show_info_for_country = tk.Label(covid_settings_frame, bg=bg, fg="white", width=15,
                                     height=1, anchor=tk.W, font=("Oxygen", 14), text="Starting country")
    show_info_for_country.grid(
        row=0, column=0, padx=0, pady=(50, 10))

    country_enter_field = tk.Entry(covid_settings_frame, bg=bg_2, fg="white", bd=0, font=(
        "Oxygen", 14), width=10, textvariable=1, justify='left')
    country_enter_field.delete(0, 'end')
    country_enter_field.grid(row=0, column=1, padx=62, pady=(50, 10))

    start_at_launch = tk.Label(covid_settings_frame, bg=bg, fg="white", width=15,
                               height=1, anchor=tk.W, font=("Oxygen", 14), text="Show on startup")
    start_at_launch.grid(row=1, column=0, padx=0, pady=5)

    start_at_launch_button = tk.Button(covid_settings_frame, bg=bg, width=50, height=23,
                                       image=on_button, activeforeground="white", activebackground=bg, bd=0, relief=SUNKEN)
    start_at_launch_button.grid(row=1, column=1, padx=0, pady=5)
    """


if __name__ == "__main__":

    def minimize_window():
        root.overrideredirect(0)
        root.iconify()

    def appear(event):
        root.overrideredirect(1)

    def callback(event):
        root.geometry("+{0}+{1}".format(event.x_root, event.y_root))

    def covid_enter(event):
        covid.configure(foreground=txt, background=bg_3)

    def covid_leave(event):
        covid.configure(foreground=txt, background=bg_2)

    def weather_enter(event):
        weather.configure(foreground=txt, background=bg_3)

    def weather_leave(event):
        weather.configure(foreground=txt, background=bg_2)

    def global_time_enter(event):
        global_time.configure(foreground=txt, background=bg_3)

    def global_time_leave(event):
        global_time.configure(foreground=txt, background=bg_2)

    def settings_enter(event):
        settings.configure(foreground=txt, background=bg_3)

    def settings_leave(event):
        settings.configure(foreground=txt, background=bg_2)

    multiprocessing.freeze_support()

    root = tk.Tk()
    root.resizable(False, False)
    root.overrideredirect(1)

    root.wm_attributes("-transparentcolor", "gray")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width/2) - 1000/2
    y_coordinate = (screen_height/2) - 600/2

    root.geometry("1000x600+%d+%d" % (x_coordinate, y_coordinate))

    bg = "#121212"
    bg_2 = "#1f1f1f"
    bg_3 = "#292929"
    txt = "#ebebeb"
    bar = "#0081cc"

    font = ("Oxygen", 12)
    font_2 = ("Oxygen", 20)

    canvas = tk.Canvas(root, width=1000, height=600,
                       bg=bg, highlightthickness=0)
    canvas.pack()

    title_bar = tk.Frame(root, bg=bg)
    title_bar.place(relwidth=1, relheight=0.055, relx=0, rely=0)

    minimize_image = tk.PhotoImage(file="images/Buttons/minimize.png")

    exit_image = tk.PhotoImage(file="images/Buttons/exit.png")

    destroy = tk.Button(title_bar, bg=bg, fg=txt, bd=0, activebackground=bg_2, activeforeground=txt,
                        relief=SUNKEN, font=("Oxygen", 12), width=50, height=35, image=exit_image, command=root.destroy)
    destroy.pack(side='right')

    minimize = tk.Button(title_bar, bg=bg, fg=txt, bd=0, activebackground=bg_2, activeforeground=txt, relief=SUNKEN, font=(
        "Oxygen", 12), width=50, height=35, image=minimize_image, command=minimize_window)
    minimize.pack(side='right')

    title_bar.bind("<Map>", appear)
    title_bar.bind("<B1-Motion>", callback)

    top_menu = tk.Frame(root, bg=bg_2)
    top_menu.place(relwidth=1, relheight=0.12, relx=0, rely=0.055)

    covid = tk.Button(top_menu, bg=bg_2, fg=txt, bd=0, activebackground=bg_3,
                      activeforeground=txt, relief=SUNKEN, width=15, height=3, font=font, text="COVID-19", command=show_covid)
    covid.pack(side='left')

    covid.bind("<Enter>", covid_enter)

    covid.bind("<Leave>", covid_leave)

    weather = tk.Button(top_menu, bg=bg_2, fg=txt, bd=0, activebackground=bg_3,
                        activeforeground=txt, relief=SUNKEN, width=15, height=3, font=font, text="WEATHER", command=show_weather)
    weather.pack(side='left')

    weather.bind("<Enter>", weather_enter)

    weather.bind("<Leave>", weather_leave)

    global_time = tk.Button(top_menu, bg=bg_2, fg=txt, bd=0, activebackground=bg_3,
                            activeforeground=txt, relief=SUNKEN, width=15, height=3, font=font, text="GLOBAL TIME", command=show_global)
    global_time.pack(side='left')

    global_time.bind("<Enter>", global_time_enter)

    global_time.bind("<Leave>", global_time_leave)

    settings = tk.Button(top_menu, bg=bg_2, fg=txt, bd=0, activebackground=bg_3,
                         activeforeground=txt, relief=SUNKEN, width=15, height=3, font=font, text="SETTINGS", command=show_settings)
    settings.pack(side='left')

    settings.bind("<Enter>", settings_enter)

    settings.bind("<Leave>", settings_leave)

    show_covid()

    root.mainloop()
