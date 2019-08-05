# linux 鸟哥的私房菜
* 测试

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
        
          
        
