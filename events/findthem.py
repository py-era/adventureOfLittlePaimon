def event_findthem(self):
    import random
    self.console.PRINT("你四处看了看.....",colors=(137, 164, 191))
    self.console.INPUT()
    self.console.PRINT("但是谁也没有来",colors=(255,0,0))
    self.console.INPUT()
    self.console.PRINT("「喂...?」",colors=(0, 188, 212))
    self.console.INPUT()
    self.console.PRINT("...?")
    self.console.INPUT()
    self.console.PRINT("「啊，能听到真是太好了」",colors=(0, 188, 212))
    self.console.PRINT("「我是...居住于此地的神明，但是...因为已经很久没有人来这里了，我的力量...很弱小了」",colors=(0, 188, 212))
    self.console.PRINT("...")
    self.console.INPUT()
    self.console.PRINT("「啊！不好意思，差点忘记让你说话了！」",colors=(0, 188, 212))
    self.console.PRINT("「就用while和input之力...」",colors=(0, 188, 212))
    while True:
        input=self.console.INPUT()
        if input=='1':
            saylist=["「这里很荒芜...但是并非什么都没有，这个世界诞生的时候似乎提供了很多”权能“....」","「这里的生灵的灵魂貌似被关押在一个叫csv的地方？这是我能窥见的一角....」","「起码还有音乐可以听？不是嘛」","「传说....可以拼接世界的权柄在一个叫event_manger的神器中....」","「你说有没有一种可能我们都是游戏里的角色？我想说的只不过是被别人打进来的字？」","「咖喱饭很好吃」"]
            self.console.PRINT(random.choice(saylist),colors=(0, 188, 212))
            self.console.INPUT()
            self.console.PRINT("和神明愉快的聊了会天...")
            self.console.INPUT()
        if input=='2':
            self.console.PRINT("她现在还没有肉身...",colors=(255,0,0))
            self.console.INPUT()
            self.console.PRINT("感受到了不解的视线.....",colors=(0, 188, 212))
        if input=='3':
            self.console.PRINT("她现在还没有肉身...",colors=(255,0,0))
            self.console.INPUT()
            self.console.PRINT("感受到了厌恶的视线.....",colors=(0, 188, 212))
        if input=='4':
            self.console.PRINT("「已经决定好出发了吗？请加油哦！」",colors=(0, 188, 212))
            self.console.INPUT()
            break
        self.console.PRINT("「你现在应该可以说话了！」",colors=(0, 188, 212))
        self.console.PRINT("「说点什么？」",colors=(0, 188, 212))
        self.console.PRINT("[1]聊天",click="1")
        self.console.PRINT("[2]杀害",click='2')
        self.console.PRINT("[3]侵犯",click='3')
        self.console.PRINT("[4]离开",click='4')
