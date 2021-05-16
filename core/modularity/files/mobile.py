class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = 0
        self.apps = []

    def power_on(self):
        self.status = 1

    def power_off(self):
        self.status = 0

    def install_app(self, app):
        self.apps.append(app)

    def uninstall_app(self, app):
        self.apps.remove(app)


huawei = MobilePhone('Huawei', 5.3, 8)
huawei.power_on()
print(huawei.status)
huawei.install_app('Twitter')
print(huawei.apps)
huawei.uninstall_app('Twitter')
print(huawei.apps)
huawei.power_off()
print(huawei.status)
