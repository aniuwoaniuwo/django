#-*-coding:utf-8-*-
from myproject.wsgi import *
from database.models import classification,data


def main():
    l=classification.objects.get_or_create(name='论文',slug='paper',administrator='张三',intro='这是大学的论文，请欣赏')[0]

    l1=data.objects.get_or_create(title='大电网日前市场负荷预测技术研究',content='本毕业设计是在许方园副教授直接指导下完成的。在毕业设计开展的每一个阶段中，许方园副教授都对我进行了耐心又详细的指导，认真检查我的设计内容。每当我遇到困难时，许方园副教授都为我提供参考书籍，并为我排忧解难，指明我在毕业设计过程中出现的问题，提出许多宝贵的修改意见。特在此向许方园副教授表示衷心的感谢！另外，在毕业设计开展期间，寸馨师姐也给我提供诸多指导和帮助，在此也表示由衷的感谢！在毕业设计内容、资料收集、软件应用、程序设计等方面，我得到了同组同学的热情帮助，也由衷向他们表示感谢！最后，我想对在这四年里帮助过我的老师们和同学们真诚地说一声谢谢！感谢你们四年来的互相陪伴和互相扶持！本次毕业设计，是大学生涯的结束，也是一个新的过渡。人生即将进入新的阶段，在此，真诚地祝福大家都能够在新征程中逐渐成长，收获成果！',slug='论文1',intro='大电网日前市场负荷预测作为电力系统负荷预测重要的一部分，是发电厂安排日开停机计划、进行机组优化组合的基础，也是调度部门进行潮流控制、实现经济调度的基础。同时，随着电力市场的发展和成熟，日前市场负荷预测已成为各售电公司开展电力交易的依据。因此，科学的负荷预测技术对电力系统许多部门起着十分重要的作用。',author='aniuwo',press='图书馆')[0]
    l1.type.add(l)
    l2 = data.objects.get_or_create(title='大电网实时市场负荷预测技术研究', slug='论文2',
                                    intro='电力系统规划和运行研究中，电力系统中短期负荷预测是非常重要的内容，它是电力系统经济和可靠运行的前提，同时也是电网规划建设的依据和基础[1]。在电力工业的发展对国民经济的影响越来越大的背景下，正确的负荷预测越来越重要，因此电力行业的网络布局和合理的运行在很大程度上由负荷预测的精度决定。',
                                    author='aniuwo', press='图书馆',relevant='电力系统短期负荷预测_张倩')[0]
    l2.type.add(l)


    h = classification.objects.get_or_create(name='个人作业', slug='homework', administrator='李四', intro='这是我大学四年的作业与写的课程论文')[0]
    h2 = data.objects.get_or_create(title='声乐论文', slug='作业1',intro='通俗歌曲演唱技法',author='aniuwo', press='图书馆')[0]
    h2.type.add(h)
    m = classification.objects.get_or_create(name='学习资料', slug='learning materials', administrator='王五',intro='这是我大学的学习资料，希望对你有用')[0]
    m2 = data.objects.get_or_create(title='继保', slug='资料1', intro='电机学的精髓都在这里', author='aniuwo', press='图书馆')[0]
    m2.type.add(m)
if __name__=='__main__':
    main()
    print('done!')



