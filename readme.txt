1���������ļ���learn-flasky
2���������⻷��
virturalenv venv
�Ӷ�������һ���ļ���
3���򿪹���Ա��cmd����̨������venv\Scripts\activate
�Ӷ����������⻷��������python��pip�ȶ�ʹ�õ���venv\lib�ڵĸ�����������ⲿ���κ�Ӱ��
4��Ȼ��pip install flask��װflask��
5����pycharm��open learn-flasky�ļ��У���Ϊ��Ŀ�ļ�
6������pycharm��VCSϵͳ��ѡ��git
7����ƺ����ļ�������.idea��venv

2015.1.11
1����װ��flask-script
2���ع����룬�ص�������Manager(app)
3����������ģʽ�����룺python hello.py runserver --host 0.0.0.0�������ε������ĵ��Զ��ܵ�½�˷�����
4���ֻ�����֤�ɹ�
		���ֻ����������192.168.0.104:5000������ʾ
5��������base.htmlģ��
6������baseģ�壬������index,user,404ҳ��
7��������form����ʹ����wtf���ٱ�����
8��ʹ����flash��������ʱ����ֱ���ڴ������������ģ�������unicodeerror���⣬���ʹ����u''�����
9�����������ݿ⣬ʹ��sqlite3��
10�������������У�ʹ��������Ǩ��