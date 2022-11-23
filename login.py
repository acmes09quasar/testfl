if __name__ == "__main__":
    hbstart = "HB_1"
    hbend = "HB_24"
    for i in adbportsjson:
        index = i["Index"]
        name = i["Name"]
        if name == hbstart or hbstart == "":
            print("start from ", hbstart)
            hbstart=""
        elif name == hbend:
            break
        else:
            print(i["Name"], "skip")
            continue
        Adbport = i["AdbPort"]
        startVirtual(index, Adbport)
        print("adbport:", Adbport)
        auto_setup(__file__, devices=getAdbPortURI(Adbport))
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

        start_app(package="com.v2ray.ang")
        poco("com.v2ray.ang:id/fab").wait(timeout=10).click()
        keyevent("HOME")
        start_app(package="pro.huobi")
        sleep(3.0)

        count = 0
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        while True:
            sleep(3.0)
            login()
            confirmPoint()
            #getPoint()
            switchAccount()
            count += 1
            if count >= 10:
                break

        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #with open(point_hb_json_file, "w", encoding='utf-8') as f:
        #    json.dump(secretjson, f, indent=4, ensure_ascii=False)
        stopVirtual(index, Adbport)
        print("end")
