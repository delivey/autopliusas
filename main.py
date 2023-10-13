from curl_cffi import requests
from bs4 import BeautifulSoup
import time


class Monitor:
    def __init__(self):
        self.base_url = "https://en.autoplius.lt/ads/used-cars?category_id=2&older_not=1&slist=2134004726&order_by=3&order_direction=DESC"

        self.headers = {
            'authority': 'en.autoplius.lt',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,pl;q=0.5',
            'cache-control': 'no-cache',
            'cookie': 'OptanonAlertBoxClosed=2023-08-03T10:00:59.286Z; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.317.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.482.486.491.494.495.501.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1769.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2913.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3104.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3299.3300.3306.3307.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5031.5231.6931.7031.7235.7831.7931.8931.9731.10231; _cc_id=d6556375c43320b15603c8356a4e6b9e; _ga_2VJ05P0R43=GS1.1.1694789890.3.0.1694789893.0.0.0; _ga=GA1.2.630108096.1691056850; saved_searches=6506b630190a3; _sharedid=ad53ba97-58f4-4a27-9017-fae3291d4d97; eupubconsent-v2=CPv66YgPv66YgAcABBENDZCsAP_AAAAAAChQGBtX_T5eb2vj-3Zct_tkaYwf55y3o2wzhhaIke8NwIeH7BoGP2MwvBV4JiQCGBAkkiKBAQVlHGBcCQAAgIgRiTKMYk2MjzNKJLJAilMbc0NYCD9mnsHT2ZCY70-uO__7v3eAAABAJAzAAQAAsACoAHIAPABAADKAGgAagA8ACIAEwAJ8AVQBWACwAG8APwAhIBEAESAI4ASwAmgBSgDAAGGAMsAbIA-IB9gH7AP8BAICLgIwARoAkoBPwCoAFzAMUAaIA1gBtADcAIhAR6AkQBOwChwFIgKbAWgAtgBcgC7wF5hABwADgASAA_AD-ANoAg4BHAC-gIfASsAmUBSACxAF5BoAYAVgDWALkEQAwArAGsAXIKgBAJBAXIKABADaAHgMgAgLkGAAgBtADwHAJgAEQAOAA8AC4AJAAfgBQADQAH8ARwAswBtADkAIAAQcAiIBHACbAFQANYAdIA8gCEAEPgJWATEAmUBQoCkwFMAKmAVUArYBXYCxAFoALoAYEAwQdA7AAWABUADkAHwAggBiAGUANAA1AB4AEQAJgAT4AqgCsAFiALgAugBiADeAH6ARABEgCWAEwAJoAUoAsQBgADDAGyAN-AfYB-gD_gIsAjABHQCSgE_ALmAXkAxQBtADcAHTAPsAiEBF4CPQEggJEASoAmQBOwChwFIAKbAVYAsUBZQC2AFyALtAXeAvMBfRAAgAAgAB4AaAA_gDaAHIAPAAjgBfQEPgKFAUmAsQBeQDAgGCEIDgACwAYgA1ACYAFMAKoAXAAxABvAEcAKUAWIAwABvgD_AJKAXMAxQBtAEQgI9ASCAlQBVgCxQFlALRAXISgNgAIAAWABwAD4AMQAeABEACYAFUALgAYoBEAESAI4AYAA2QB-AFzAMUAfYBEwCLwEegJEAWKAsoBbAC8yQAsAC4A2gCAAEHAISARwAqAB2wErAKTAYEUgXAALAAqAByAD4AQAAxgBoAGoAPAAiABMACeAFUALAAYgA_QCIAIkAUoAsQBgADZgH4AfoBFgCMAEdAJKAXMAvIBigDaAG4APsAiYBF4CPQEiAJ2AUOApABTYCrAFigLQAWwAuQBdoC8wF9FAD4AFwASAAyAB-AFYANoAfwBHADaAHIAPAAfYBAACDgEJAIqATYA14B2wDyAH_ARCAmIBTACpAFTAK7AXQAvIBgQDBA.f_gAAAAAAAAA; __gfp_64b=5q.QLclQrHGKq85yIDFEQNQ5teK1owYlIJMOaSxg1fn.j7|1691056859; _gid=GA1.2.630616567.1696533264; _pbjs_userid_consent_data=3527713662937278; PHPSESSID=rjmvp86nstei6oj5stc26i0p17; __cf_bm=MMtAMjIqVepAE5pYMBURHx0Of9VfAaJJ6jNqyvAZ_Lo-1696594763-0-AUjprZUi7zbvna/PFnzFmYSW5sgAyx1PYxnfx88Cq5gsBsTkQ1gccq85Mo41ykgGcmZxDmxcd8W/k30lHfDu0xA=; __gads=ID=6997b11701785943:T=1691056864:RT=1696594765:S=ALNI_MaF9VRXT-0fDMakGUhW_adXHyrKjw; __gpi=UID=00000c77770dfe46:T=1691056864:RT=1696594765:S=ALNI_Ma7nPzuvhWfjkIb7cF2hwhZLQgBhw; z=1696594767651ffb4f91f42; stpdOrigin={"origin":"referral"}; banners_139=eNqzNjc1M9UxNLM0M7MwNDQ30NEBACN8A6Q=; _gat=1; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+06+2023+15%3A23%3A39+GMT%2B0300+(Eastern+European+Summer+Time)&version=202306.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3902b780-4f00-45fd-9f53-8d36e572dfe6&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CSTACK42%3A1&geolocation=LT%3BVL&AwaitingReconsent=false; cto_bidid=M5MY419LcnZwVlElMkJRRzNjcGVlZ09oRUpISHhlWk8xSVkzYTJsUkw1biUyRk1sTzU1RGVYQndGNnFBbGdRUnhUeTBrREVQRVZLUThNRXNGazZseVppViUyQk5VbmdyR2JiZFFLMzFFaDMlMkJJcFljMnVGZGRjJTNE; cto_bundle=LYXH2l93OSUyQmMzUDRhd3ZueUZleDZwejYyRjJ5N1ZmdWZOR3RHZ2dDQnpqQUdBeW9UclR0VkpJVHRhZjAyUmRPZDh1WUFhaXdRUGJYUGt0WHVmRGslMkJEWnVESURFd1FReFZlYyUyRkxhYkl5ZmRtdDNSSVhvVlJTSHQzWDVFcWJrMCUyRmRrbVBZZ1NQSTl6NFFLOE8zZUMxQXlhJTJGdWJnJTNEJTNE',
            'pragma': 'no-cache',
            'referer': 'https://en.autoplius.lt/ads/used-cars?category_id=2&older_not=1',
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

    def get_minutes_ago_from_date(self, date):
        try:
            number = int(date.split(" ")[0])
            if "Less than" in date:
                return 1
            if " days ago" in date:
                return number * 24 * 60
            if " h ago" in date:
                return number * 60
            if " h" in date and " min ago" in date:
                minutes = number * 60 + int(date.split(" ")[2])
                return minutes
            return number
        except:
            print("nepavyko gauti minutes ago is date")
            print(date)
            return False

    def get_all_cars(self):
        r = requests.get(self.base_url, headers=self.headers,
                         impersonate="chrome110")
        soup = BeautifulSoup(r.text, "html.parser")
        cars = soup.find_all("a", class_="announcement-item")
        return cars

    def get_filtered_cars(self, cars):
        filtered_cars = []
        for car in cars:
            badge = car.find("div", class_="badge-new")
            if not badge:
                continue

            date = badge.text
            minutes_ago = self.get_minutes_ago_from_date(date)
            if minutes_ago == False:
                return
            url = car.get("href")
            filtered_cars.append({
                "url": url,
                "minutes_ago": minutes_ago,
                "found_on": int(time.time())
            })
        return filtered_cars

    def get_newest_car(self):
        all_cars = self.get_all_cars()
        filtered_cars = self.get_filtered_cars(all_cars)
        if not filtered_cars or len(filtered_cars) == 0:
            return False
        newest_cars = sorted(
            filtered_cars, key=lambda car: car['minutes_ago'])
        # for car in newest_cars:
        #     print(
        #         f"radau masina: {car['url']}, pries {car['minutes_ago']} minutes ikelta")
        newest_car = newest_cars[0]
        return newest_car

    def car_matches_criteria(self, newest, last):
        if newest["url"] == last["url"]:
            return False
        current_time = int(time.time())
        minutes_ago = (current_time - last["found_on"]) / 60
        if newest['minutes_ago'] > minutes_ago + last['minutes_ago']:
            return False
        return True

    def monitor(self):
        newest_car = self.get_newest_car()
        print(
            f"pirma naujausia masina - {newest_car['url']}, pries {newest_car['minutes_ago']} minutes ikelta")
        while True:
            time.sleep(60)
            new_newest_car = self.get_newest_car()
            if not new_newest_car:
                print("jokiu masinu bbd")
                continue
            if self.car_matches_criteria(new_newest_car, newest_car):
                print("\nnauja masina radau krc")
                print(new_newest_car["url"])
                print(f"pries {new_newest_car['minutes_ago']} minutes ikelta")
            newest_car = new_newest_car


print("pradedam")
monitor = Monitor()
monitor.monitor()
