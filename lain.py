#001 什么是变量
#----在程序中可以改变的量就是变量
# 变量的语法格式： 变量名 = 值

#002变量的命名规则
#-可以使用字母数字和下划线
#-不能纯数字开头
#-不能用纯数字
#-不能有特殊字符
#-不能用python关键字

#003变量的命名习惯
#-多个单词之间可以使用大小驼峰
#-多个单词之间可以使用下划线进行连接
#-变量名不要所有字母大写
#-不要用中文
#-见名知意

#004Python的数据类型
#----数字型
 #--整数型(int)
 #--浮点型(float)
 #--布尔型(bool)
   #-True(真)
   #-Flase(假)
#----非数字型
 #--字符串(str)
 #--列表(list)
 #--元组(tuple)
 #--集合(set)
 #--字典(dict)
#----空型
 #None  首字母大写 空


#005格式化字符有哪些？
# %d 要格式化整数
# %s 格式化字符串
# %f 格式化浮点型
# %%  输出一个%

#006数据类型的转换有哪些？
# 转化为str()
# 转化为int()
# 转化为flaot()

#007转义字符有哪些？
# \n(换行)   \t(空格)   r(禁止转义)

###008break和contiune的区别
#--001break和contiune是python的两个关键字
#--002break是终止循环的执行，contiune是结束本次循环，
#-- 继续下一次循环
#--003break和contiune只能用在循环当中

###009while循环和for循环的不同、
#---while循环主要是指定次数的循环
#---for循环最主要的作用就是遍历
#---while循环和for循环可以相互转换

##010在python中，所有非数字类型变量都有以下特点：
#-01都是一个序列
#-02通过变量名[索引]方式取值
#-03通过for循环遍历
#-可以使用公共方法(计算长度，最大值和最小值)

11##list三个增加的方法
#--insert()   往置定位插入数据
#--append()   往末尾追加数据
#--extend()   追加另外一个列表的值

12##list中的5个删除方法
#---remove(值)  根据指定的值进行删除
#---pop()   如果有索引删除指定位置的值，没有删除末尾元素


13#list中升序降序逆置的方法
#---sort  升序
#---sort(reverse=True) 降序
#---reverse  逆置

14#list修改值得方法
list[索引] = 值


15###元组和列表的区别
#--列表是可变的，元组是不可变的
#--元组不可增删改，存储数据更加安全
#--元组和列表之间可以相互转换
#--元组和列表之间声明不同(括号)

16##集合和列表的区别？
##--集合中所有成员是无序的，列表中成员是有序的
##--集合中成员的值不能重复，列表中成员值可以重复

17###python对列表去重的四种方法：
#第一种方式：使用keys()方法进行去重
#第二种使用set无序不重复的特性去重
#第三种方式for循环遍历判断在不在空列表进行去重
#第四种使用set特性去重，然后利用sort特性在按照索引排序去重

18###冒泡排序
##什么是冒泡排序？
#冒泡排序就是将一堆杂乱无序的元素，通过方法或者函数，将他们变为有序的，
# 就像水中冒泡一样，将其中最大或者最小的元素，一个一个冒泡出来

19###冒泡排序的原理
#冒泡排序就是将第一个元素与后面的元素进行比较大小，选出最大或者最小的一个，然后
#继续跟后面的元素进行比较，直至比较到最后一个，也就是说通过第一轮的比较，列表末尾
#的元素应该就是这个列表中最大或者最小的元素，后边以此类推重复进行以上比较操作

20###函数的作用
###-让代码不要重复冗余
###-提高代码的利用率
###-提高开发的效率和时间


21###类和对象的关系(面试里重点)
#--类是静态的，是不能直接使用的，要想使用得创建对象
#--类是更大的封装(封装函数)
#--先有类后有对象，类只有一个，对象可以有很多个
#--类是抽象的，对象是根据类创造出的具体的存在
#--类里面定义几个方法，创建对象调用方法的时候，就能调用几个，不可能多也不可能少

22###实例和实例化
###什么是实例：通过类创建的对象就是实例
###什么是实例化：创建对象的动作或者过程叫做实例化

23###self参数的作用
#----self可以在方法的内部定义和使用
#----self可以在方法的内部嵌套调用
#----self只能在类的内部使用，外部无法使用
#----类里边使用属性和方法，要用self调用使用
#----self真正的作用就是相当于实例或者对象自己


24###init的作用
#---定义类中的属性
#---为属性进行赋值
#---init方法一旦有形参，对象实例化的时候就必须提供实参
#---为了避免实例化的时候必须提供实参，init形参可以设置缺省值

25###设计类的三个要素：类名，属性，方法


26面向对象的三大特性
#封装---根据职责将属性和方法封装到一个抽象的类中
#继承---实现代码的重用，相同的代码不需要重复的编写
#多态---不同的对象调用相同的方法，产生不同的结果，增加代码灵活度


27方法的重写
#--覆盖父类的方法
#--子类中出现和父类相同的方法，那么在子类中相同的方法会把父类相同的方法覆盖
#--扩展父类的方法
#--如果父类的方法不能满足子类需求，子类可以在父类方法基础上增加新的功能

28Python中装饰器有哪些？
#@classmothod 修饰类方法的
#@parameterized  参数化的装饰器
#装饰器是通过传入参数的方式来增强函数的功能，它是一种函数的函数，比较简洁
#方便，装饰器一般添加到类或者方法上边



29unittest是什么？
#---是python自带的单元测试框架，具备编写测试用例，组织测试用例，执行测试用例
#---输出测试报告等自动化框架的条件


30unittest主要包含的内容
#----TestCase(测试用例)
#----TestSuite(测试套件)
#----TextTestRunner(执行用例)
#---TestLoader(自动加载扫描多个测试用例模块放入组件里)
#----FixTrue(类级别)



31为什么使用unittest框架
#---0能够组织多个测试用例执行
#---提供丰富的断言
#---提供参数化技术，实现数据和业务的分离，方便后期的维护
#---生成测试报告



32#-----什么是自动化测试？
#---程序代替人工进行测试的过程，就是自动化测试

###自动化测试能解决什么问题？
#---针对之前的老功能进行测试（针对上个版本回归测试）
#——-兼容性的测试
#---实例化不同的浏览器对象针对不同的浏览器进行操作
#---性能测试，通过一个工具模拟多个用户实现并发操作
#---提高工作的效率，保证产品的质量


33####自动化测试的优点？
#---自动化测试能在较短的时间内执行更多的测试用例
#---自动化测试能够减少人为的错误、
#---自动化测试可以重复执行

34####自动化的误区
#---可以完全代替手工
#---自动化测试一定比手工厉害
#---自动化测试可以发现更多的bug

35###自动化测试分为三类
#---第一类：web自动化(UI)   python + selenium +unittest
#---第二类：app自动化(UI)   python + appium + unittest
#---第三类：接口自动化  python + requests + unittest

36###什么是web自动化？
#----针对的更多web端，页面内容以及页面的元素进行自动化测试的过程

37###什么项目适合自动化测试
#---需求变更不频繁
#---项目周期长的
#---项目需要回归测试

38####selenium的工作原理(重点)？
#---实例化浏览器驱动对象，代码脚本通过浏览器驱动对象向浏览器发
#---出指令，浏览器接收到指令后根据指令做出操作，结束之后再返回
#---给浏览器驱动对象，浏览器驱动对象再返回控制台

39####八大元素的定位(核心)
# id定位
# name定位
# class_name定位、
# tag_name
# link_text定位
# partail_link_text
# xpath定位
#  css定位


40###请你描述一下自动化测试的流程？（你们公司如何开展自动化测试的）
#---1编写自动化测试计划
#---2设计自动化测试用例
#---3搭建和编写自动化测试框架以及脚本
#---4调试和维护
#---5后期脚本跟踪升级和维护

41###你是如何编写自动化测试用例的？
#----1用例是自动化测试工程师自己设计的，以业务的基本流程为主
#----（登录---完成----退出）
#----2从系统测试用例进行筛选或者由业务工程师进行提供


42###一般你的自动化执行策略在什么时候？
#----自动化一般设置定时执行，设置的时间一般晚上12点，执行完毕
#----自动发送邮件和报告

43###自动化测试发现的bug多吗？
#---不多，因为之前项目组已经通过基本的功能测试，通过之后再
#---进行自动化测试，而编写后续版本执行自动化测试，主要是保证
#---已经通过的功能在新版本中没有问题

44###你觉得自动化的价值在哪里？（你们回公司为什么要做自动化）
#----引用自动化测试后，能代替大量繁琐的回归测试，把业务人员解放
#----出来，继而让业务人员把主要精力集中在复杂的业务功能模块，自动化
#----测试一般是在稳定下来的功能进行自动化测试的，能保证不会因为产品
#---更新导致之前稳定下来的功能表出现bug



45###自动化测试有没有误报过bug?产生误报咋办？
#---有误报过，有时候可能存在自动化测试报告中显示发现了bug,但是
#---手工测试的时候，bug不存在

#误报的原因：
#---元素定位不稳定，需要尽量提高脚本的稳定性
#---开发更新了页面没有及时通知我们，及时沟通


46###自动化过程中有没有遇见问题，如何解决这些问题？
#----自动化过程中偶尔出现误报
#----开发频繁的变更页面，经常的修改代码
#----自动化测试代码维护比较麻烦


47###你做自动化用什么框架？


48###自动化测试过程中，一般完成什么类型的测试？自动化测试的覆盖率多少？
##主要是回归测试和冒烟测试，回归测试主要是写一些功能稳定的场景，用过
##自动化手段实现，节约测试时间，因为自动化测试用例也是在不断的更新
##和迭代
#覆盖率没有刻意统计，大概（30-40）%

49###如果一个元素无法定位，你一般会考虑哪方面的原因？
#---页面加载过慢，加等待时间
#---页面frame框架，需要先跳入frame框架，再定位
#---该元素可能是动态的，定位需要优化，可以使用部分元素定位或
#---用过父节点或兄弟节点定位
#---可能识别了该元素，但是不能操作，元素不可用，不可写，需要js前置
#的操作完成


50###如果遇到frame框架如何处理？
#--先用driver.switch_to.frame() 跳转进frame
#--然后再操作该元素，操作完成使用# driver.switch_to.default_content()
#--跳转出来


51###你是如何处理弹框的？
#---使用driver.switch_to.alert方法跳转到alert弹窗口
#--然后通过accept点击确定按钮，通过dismiss点击取消，通过text()获取弹框文本


52###如何处理下拉框
#--定位到元素
#--把定位的元素转化为select对象，select = select(element)
#--通过下标或文本选中下拉框（索引，值，文本）

53###自动化过程中遇到的异常有哪些？
#--NoSuchElementExpection:找不到元素异常
#--TimeOutExpection:超时异常
#--ElementNoVisibleExpection:元素不可见异常
#--NoSuchFrameExpection:没有frame异常

54##自动化如何截图？
#---get_screeshot_as_file(文件路径)

55##自动化如何实现文件上传？
#直接使用send_keys(路径)

56###你写的脚本能在不同的浏览器上运行吗
#---可以，可以在IE，谷歌，火狐上运行，需要下载不同的浏览器驱动，实例化不同的浏览器对象


57###如何实现selenium的执行速度
#---优化测试用例,尽量少用设置等待时间sleep,尽量不用隐式等待，使用显示等待
#——--减少不必要的操作步骤，如果需要经过三四步才能打开网页，可以直接通过网址打开
#---设置多线程并发


58###浏览器的常用方法
#back()   后退----模拟浏览器后退按钮
#forward() 前进 ----模拟浏览器前进
#refresh()  刷新  -----模拟浏览器刷新按钮
#close()   关闭当前窗口   ----模拟浏览器关闭按钮
#quit()  关闭浏览器驱动对象  ---关闭所有程序启动的窗口

59###CSS的定位策略（重点）
#----id选择器
#----class选择器
#----元素选择器
#----属性选择器
#---层级选择器


60###xpath的定位策略（方法）：
#----路径定位
#---属性定位
#---属性和逻辑结合定位
#---属性和层级结合定位


61###获取元素信息常用的方法：
# ---size  获取元素的大小   返回的是一个字典   里边包含高度和宽度
# ---text  获取元素的文本内容
# ---get_attrbute("attrbute")  获取元素属性名称的属性值


62###三个判断元素状态的方法
# ----is_displayed()      判断元素是否可见
# ----is_enabled()       判断元素是否可用
# --- is_selected()      判断复选框或者单选框是否选中


63# ----鼠标的操作
# ----实现方式（步骤）
# ----第一步：需要导入ActionChains类
# ----第二步：通过ActionChains类实例化一个鼠标对象
# ----第三步：调用鼠标的事件方法
# ----第四步：调用鼠标的执行方法

64###显示等待和隐式等待的区别(重点中的重点)：
#-1抛出的异常不一样，隐式等待抛出的异常noSuchElementExpection(找不到元素异常)
#显示等待抛出的异常timeOutExpection(超时异常)

#-2作用域不一样，隐式等待对所有元素定位方法有效，只需要定义一次，而显示等待只针对单个元素

#-3显示等待不需要等待真个页面加载完成，显示等待效率更高，工作当中推荐显示等待



65###说一说app自动化你常用的定位工具是什么？
#----uiAutomatorViewer定位工具


66###appium的工作原理
#---通过客户端发送自动化指令给appium服务器，appium服务器在接收到客户端
#---指令后，将指令转换为移动端能够识别的指令，然后发送给移动端设备，并对
#---移动端设备进行操作，以此完成测试流程

67###appium的局限性
#——--不支持安卓4.2一下版本

68###appium可能遇见哪些错误
#--错误1-可能找不到adb,android-sdk环境变量路径配置出错
#--错误2-无法创建会话连接，连接拒绝  appium确保打开
#--错误3-查找元素失败，更换定位方式


69###appium和selenium的区别
#---appium是app端自动化，selenium是web端自动化
#---appium继承了webdriver



70###自动化过程中项目搭建的实战框架
#---base(包)#---封装po基类
#---page(包)#---封装po页面对象
#---script #---定义测试用例脚本
#---data#---存放测试数据
#---report#---存放测试报告
#---log #存放日志
#----img #存放截图
#----config.py#存放项目的配置信息
#----untils#存放定义工具类


71###什么是po模式
#--Page Object 模式是selenium中的一种测试模式
#--主要是将每一个页面设计成一个class,其中包含页面中需要测试的元素，这样
#--在selenium中测试页面可以通过页面类来获取元素，这样巧妙的避免了当页面元素
#或id或者位置变化时，需要修改测试也class中的属性
#--po模式是一种自动化测试设计模式，将页面和业务操作分开，分离测试对象和测试脚本
#--，提高用例的可维护性


72###adb命令：
#---adb devices  查看设备
#---adb kill-server  结束服务
#---adb start-server  开启服务
#---adb logcat  查看日志
#---adb logcat | find "关键字"
#---adb shell top -m -10  查看当前进程（监控相关资源）
73###查看包名和界面名
# adb shell dumpsys window windows | findstr  mFocusedApp
# adb shell dumpsys window | findstr "usedApp"


74###monkey  猴子
#----monkey集成在adb工具当中的，主要是做稳定性测试的
#----测试app会不会崩溃(crash)的情况
#---原理：相当于让一只猴子来随机操作app,所有的操作情况都可能
#---出现，长时间的操作来测试app会不会出现问题
75#monkey常用测参数
#----  -p 参数   对指定的app随机操作
#---- adb shell monkey -p 包名  随机次数
#----  -v 参数   表示的是记录信息的级别
#-----adb shell monkey -p 包名 -v 100 默认级别
#----- -s 参数   用于指定伪随机事件，主要作用复现上次的问题
#-----adb shell monkey -p 包名 -v - v -s 100










