# -*- coding: utf-8 -*-


from scrapy import Item, Field

class YouyuanItem(Item):
    uid        = Field()
    url        = Field()  #头像url
    nickame    = Field()  #昵称
    age        = Field()  #年龄
    address    = Field()  #住址
    xueli      = Field()  #学历
    xinzi      = Field()  #薪资
    detailUrl  = Field()  #详细信息 url


class UserDetailItem(Item):
    uid         = Field()
    url         = Field()   #头像url
    nickame     = Field()   #昵称
    age         = Field()   #年龄
    address     = Field()   #住址
    tags        = Field()   #爱好标签
#照片展示
    smallPhotos = Field()   #图片展示
#个人资料
    dubai       = Field()   #内心独白
#详细资料
    jiguan      = Field()   #籍贯
    weight      = Field()   #体重
    xueli       = Field()   #学历
    xinzi       = Field()   #薪资
    getBaby     = Field()   #是否想要小孩：保密
    sexType     = Field()   #喜欢的异性类型：保密
    tongju      = Field()   #是否愿意与父母同住：保密
    marriage    = Field()   #婚姻：保密
    height      = Field()   #身高: 保密
    work        = Field()   #职业：保密
    house       = Field()   #住房：保密
    yidiLove    = Field()   #能否接受异地恋：保密
    foreSex     = Field()   #能否接受婚前性行为：保密
    meili       = Field()   #最有魅力的部位：笑容
#征友条件
    op_city     = Field()   #所在地区：不限
    op_height   = Field()   #身高： 不限
    op_income   = Field()   #收入：保密
    op_age      = Field()   #年龄： 不限
    op_xueli    = Field()   #学历： 不限


