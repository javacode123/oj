# linux 鸟哥的私房菜
* 文件

    * 文件权限  
    
        ls -all : 查看当前路径下文件详细信息  
        
        drwxr-xr-x  6 zjl  staff  192 Jul  6 16:24 .  
        drwxr-xr-x  9 zjl  staff  288 Jun 28 22:07 ..  
        drwxr-xr-x  6 zjl  staff  192 Jul  6 16:10 .idea  
        -rw-r--r--  1 zjl  staff   71 Jul  6 16:24 learn_linux.MD  
        drwxr-xr-x  4 zjl  staff  128 Jul  6 13:30 leetcode  
        drwxr-xr-x  4 zjl  staff  128 Jun 28 23:22 swordOffer  
        
        第一列第一个字符 'd' 或 '-' 表示文件或者文件，接着三个字符表示文件所有者的权限，读 'r', 写 'w', 执行 'x'，接着三个是同一用户组，最后三个其他用户
        第二列是文件链接数  
        第三列是文件所属用户  
        第四列是文件所属用户组  
        第五列是文件大小  
        第六列是文件更新日期  
        第七列是文件名  
        
        修改文件权限
        
        权限数字对照表 r:4 w:2 x:1
        chmod 763 .bashrc: 表示对于 .bashrc 文件，文件所属者权限 7(4+2+1 r,w,x), 文件所属用户组权限是 6(4+2 r,w), 其他人权限是 3(2+1 w,x)
        
    * 文件查看
        
        cat -n test.txt : 显示行号和内容 
        
        more : 对于文件不能一行展示的使用 more 命令
        more test.txt
            空格     : 下一页
            q       : 退出
            Enter   : 下一行
            b       : 上一页
            /字符串  ： 向下查找字符串
        
        less : 对 more 的扩展
        less test.txt
            空格     ：下一页
            enter   ： 下一行
            /字符串  ：向下搜索
            ?字符串  ：向上搜索
            q       : 退出
            b       : 上一页    
          
        tail : 查看文件尾部
        tail -f p.txt : 刷新输出后 10 行
    
    * 文件查找
    
        locate p.py : 是由已经建立的文件索引库查找，但有时需要更新数据库
        
        find : 文件查找，常用
        find -name p.py : 查找文件名 p.py， 默认从当前目录开始
        find . -name p.py : 从当前目录开始向后招
        find / -name p.py : 从根目录查找
        find / -name "*.py" : 查找所有 .py 文件
        find / -name cp -type d : 查找文件夹 cp 
    
    * 文件系统
        
        索引式文件系统：在 linux 中每个文件都对应一个 inode, 里面存储了文件的属性、权限等信息, 同时存在一个指向数据区的指针, 通过指针链接到数据, 称之为索引文件系统。
        
* vim 操作
    
    * 一般命令模式，编辑模式（i/o/a 进入编辑模式），命令模式（esc 返回到一般命令模式）
    * 一般命令模式：
        
        :n<<Enter>>   跳转到 n 行
        n<<space>>    按下数字后按空格，从当前位置后移 n 个字符
        gg            回到第一行  
        n<<Enter>>    n 为数字，光标向下移动 n 行  
        G             移动到文件最后一行  
        /word         向光标之下查找字符串 word, 按 n 查找下一个匹配项  
        ?word         向光标之上查找字符串 word,  
        n             重复前一个查找动作  
        :n1,n2s/word1/word2/g   从 n1 行到 n2 行, 将 word1 替换为 word2  
        :1,$s/word1/word2/g     从第一行到最后一行查找 word1, 将 word1 替换为 word2  
        :1,$s/word1/word2/gc    从第一行到最后一行查找 word1, 将 word1 替换为 word2, 替换之前提示用户是否执行确认操作  
        
        x             向后删除一个字符  
        X             向前删除一个字符  
        nx            向后删除 n 个字符  
        dd            删除(剪切)光标所在的行  
        ndd           n 为数字, 连续向后删除 n 行  
        yy            复制光标所在行的数据  
        nyy           复制光标向下 n 行  
        p             将已经复制的内容在光标下一行粘贴  
        P             将已经复制的内容在当前行粘贴
        u             回复前一个操作  
        
    * 命令行模式：
    
        :w            将编辑数据写入硬盘  
        :q            退出 vi  
        :q!           强制退出  
        :wq           退出并保存  
        :set nu       显示行号  
        :set nonu     取消行号   
        :w 文件名      文件另存为  
        
* Bash

   * env: 查看环境变量  
   * export 变量名称: 将自定义变量转换成环境变量，让子进程使用
   * echo $name: 输出变量 name 的值
   * &: 任务管理，将命令变成后台任务  
   * ls > a.txt, ls >> a.txt: 输出到文件，分别为覆盖和追加
   * 1>, 2>: 分别为标准输出和错误输出
   * find / -name .bashrc 1>des.txt 2>err.txt: 对于 permission denied 信息会输出到 err.txt
   * find / -name .bashrc &>err.txt: 标准输出和错误输出均写入同一个文件


* 正则表达式

   * ^#  以 # 开头的一行
   * $!  以 ! 结尾的一行
   * .   仅有一个字符，例如查找 (abe)(ace)(ade) 使用 a.e
   * [abz] 仅有一个待查找的字符
   * [0-9] 0-9 的十个字符中，仅有一个待查找的字符
   * t[^A-Z] t 后面一个字符不是大写字母
   * go\{3, 5\}  g 后面有两个到五个连续的 o
  
* shell script

  * if then  
  ```
    #!/bin/bash
    read -p 'input name' name
    
    if [ $name == "zjl" ]; then
        echo $name
    else
        echo 'error'
    fi
  ```
  * while
  ```
    #!/bin/bash
    s=0
    i=0
    while [ "${i}" != "${1}" ]
    do
        s=$((${s} + ${i}))
        i=$((${i} + 1))
    done
    
    echo ${s}
  ```
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
