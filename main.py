import requests
from bs4 import BeautifulSoup
import time
from notify import notify


class Monitor:
    def __init__(self):
        self.base_url = "https://autoplius.lt/paieska/naudoti-automobiliai"
        self.headers = {
            'authority': 'autoplius.lt',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,pl;q=0.5',
            'cache-control': 'no-cache',
            'cookie': '_sharedid=ad53ba97-58f4-4a27-9017-fae3291d4d97; _cc_id=d6556375c43320b15603c8356a4e6b9e; cto_bundle=oUaiXV93OSUyQmMzUDRhd3ZueUZleDZwejYyRndKSlJpUzNaMVpLWmRYZmttMGRuQyUyRkElMkZuVWY4dHM5YXcyc2FiayUyQk9KSU50QmU1ZWk2UTJsSVM2SzVuQzNMN21LOXR3T1hqdUolMkJRMlhrOXZBJTJGeFNJU3RQczU5T1dLVHFNckRXVTlQQ3VlbTA1JTJGaURvSFJRNmxSa0xLVGxGczRCUSUzRCUzRA; cto_bidid=6k_dcV9LcnZwVlElMkJRRzNjcGVlZ09oRUpISHhlWk8xSVkzYTJsUkw1biUyRk1sTzU1RGVYQndGNnFBbGdRUnhUeTBrREVQRVZLUThNRXNGazZseVppViUyQk5VbmdyTjZhMUlvWjI4czBZZVRkMjJRWWdUOCUzRA; _ga_2VJ05P0R43=GS1.1.1694789890.3.0.1694789893.0.0.0; _ga=GA1.2.630108096.1691056850; _sharedid=ad53ba97-58f4-4a27-9017-fae3291d4d97; saved_searches=6520507c74288; __gfp_64b=tXocQ0LlQr9MoxGsIe18HKyWludIzpWHXh2pCCocT_r.B7|1691056859; OptanonAlertBoxClosed=2023-10-10T19:16:35.504Z; eupubconsent-v2=CPzbCIgPzbCIgAcABBENDaCsAP_AAEPAAChQGBtX_T5eb2vj-3ZcN_tkaYwP55y3o2wzhhaIEe8NwIeH7BoGJ2MwvBV4JiACGBAkkiKBAQVlHGBcCQAAgIgRiSKMYk2MjzNKJLJAilMbM0NYCD9mnsHT2ZCY70-uO__zvneBggBJgoXEADYEhATLRhBAgAGEYQFQAgAoAEgKADCEAEBOwKAj1gIAAACAAEAAAAAIIgAQAACQBIRAAAAYCAQAAQCAAEAAoQCAAiQABYAWgAEAAoBoSAUUAQgGEGBCBEKYEAQCAwAYAFQALwA7gEAAIwAksNADACsAawBcggASACoAF4AdwCAAEYANQAjsBJYC3REAMAKwBrAFyCgAYAKgBtADwFQAgEggLkGABAAVACuAG0APAZABAXIA.f_gACHgAAAAA; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.317.320.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.482.486.491.494.495.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1769.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2913.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3104.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3299.3300.3306.3307.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5031.5231.6931.7031.7235.7831.7931.8931.9731.10231.10631.10831.11031.11531.12831.13632.13731.14237; _pbjs_userid_consent_data=3210071649112036; _gid=GA1.2.1003901306.1697117111; __gads=ID=6997b11701785943:T=1691056864:RT=1697201011:S=ALNI_MaF9VRXT-0fDMakGUhW_adXHyrKjw; __gpi=UID=00000c77770dfe46:T=1691056864:RT=1697201011:S=ALNI_Ma7nPzuvhWfjkIb7cF2hwhZLQgBhw; PHPSESSID=kf3ah2m59i52be5k32dl3hrte9; __cf_bm=UN1GfEtlBuJCUO0JEHRLnHkHw9Ypell7v83d7Hg9QC4-1697202558-0-AdkJNLnVJyEuRW+ImzR1G2Bu2RmvEpf8krf/Hc7Jm+ogXnpYmVfbfE8ybulwTNWv2YgYpwg0UjyHz8ghsVulw14=; stpdOrigin={"origin":"direct"}; _gat=1; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+13+2023+16%3A09%3A28+GMT%2B0300+(Eastern+European+Summer+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3902b780-4f00-45fd-9f53-8d36e572dfe6&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CSTACK42%3A1&geolocation=LT%3BVL&AwaitingReconsent=false; cto_bidid=SvMwAl9LcnZwVlElMkJRRzNjcGVlZ09oRUpISHhlWk8xSVkzYTJsUkw1biUyRk1sTzU1RGVYQndGNnFBbGdRUnhUeTBrREVQRWl4MEtYVVlVOHhMT1RVTnNvZzVCVjI2QkZHVUpNSkNiMW5reVpIQXV6WGRlOEdCR3lEMzUlMkZhZWNSQUc0eiUyQjdsOGMlMkZPZ0FPUmIzUlJUejI3TDFvRk5BJTNEJTNE; cto_bundle=1CdCxF93OSUyQmMzUDRhd3ZueUZleDZwejYyRjVxS2dheTFaSzlxUWhoNjE3VnJ3YlJSN3FtRDhpR1lOR053cE94aWdEd21oUkRHdmhOek4wdlJTbHlncHpGdFFYaHpFaGZwY2FYNnM0Q3I1cVJ4cllERkkwaFpHWnh0dG1zaGhSbURlTE53dFd2JTJCU0RFMktCY1FVJTJGZUFyQks0cWZ2elhsVk56cjN1MXI3SERmbUZ1Rlp5ZTBKZlhKTno5VWZoRWlaQWt5WnVCVk9wMTJQR3lLZkVMY1dnTSUyRnJhYkElM0QlM0Q',
            'pragma': 'no-cache',
            'referer': 'https://autoplius.lt/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        self.cars = []
        self.seen_cars = []

    def get_minutes_from_text(self, text):
        if "min" not in text:
            return 999
        if text == "Mažiau nei prieš minutę":
            return 0
        numbers = [int(s) for s in text.split() if s.isdigit()]
        if len(numbers) == 0:
            print("neradau laiko cia??: ", text)
            return 999
        return numbers[0]

    def get_latest_cars(self):
        response = requests.get(self.base_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        car_urls = []
        cars = soup.find_all("a", class_="promoted-announcement")
        for car in cars:
            laikas = car.find(
                "div", class_="announcement-badge badge-new").text
            minutes = self.get_minutes_from_text(laikas)
            # jei jau yra masinu ir masina yra senesne nei 1 minutes, tai praleidziam
            if len(self.seen_cars) != 0 and minutes > 1:
                continue
            car_urls.append(car["href"])
        return car_urls

    def get_new_cars(self, new_cars):
        new_cars = [car for car in new_cars if car not in self.cars]
        return new_cars

    def monitor(self):
        self.cars = self.get_latest_cars()
        self.seen_cars = self.cars.copy()
        print(f"pradedam, radau {len(self.cars)} masinas")
        while True:
            updated_cars = self.get_latest_cars()
            new_cars = self.get_new_cars(updated_cars)
            for car in new_cars:
                if car in self.seen_cars:
                    continue
                self.seen_cars.append(car)
                print(f"radau nauja: {car}")
                notify(car)
            self.cars = updated_cars
            time.sleep(30)
            print("naujas ciklas")


monitor = Monitor()
monitor.monitor()
