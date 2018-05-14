#!/bin/bash

#=====================================================================
#   
#   File：：install.sh
#   Author：renyi
#   Date：2018/04/01
#   Description：在最小化centos6.9下安装Python及其依赖组件,并配置环境变量
#
#=====================================================================
#
#===  定义安装相关的文件路径，文件名  ============
# define  directories and names
version="1.0.0"
work_dir=`pwd`
install_dir="usr/local/python"
# display UI（展示界面logo和提示信息及主menu）
display_logo(){
	echo "                                   .. .vr"
	echo "                                 qBMBBBMBMY"
	echo "                                8BBBBBOBMBMv"
	echo "                              iMBMM5vOY:BMBBv"
	echo "              .r,             OBM;   .: rBBBBBY"
	echo "              vUL             7BB   .;7. LBMMBBM."
	echo "             .@Wwz.           :uvir .i:.iLMOMOBM.."
	echo "              vv::r;             iY. ...rv,@arqiao."
	echo "               Li. i:             v:.::::7vOBBMBL.."
	echo "               ,i7: vSUi,         :M7.:.,:u08OP. ."
	echo "                 .N2k5u1ju7,..     BMGiiL7   ,i,i."
        echo "                  :rLjFYjvjLY7r::.  ;v  vr... rE8q;.:,,"	
	echo "                 751jSLXPFu5uU@guohezou.,1vjY2E8@Yizero."
	echo "     .;MBZ;iiMBMBMMOBBBu ,           1OkS1F1X5kPP112F51kU"
	echo "                 BB:FMu rkM8Eq0PFjF15FZ0Xu15F25uuLuu25Gi."
	echo "               ivSvvXL    :v58ZOGZXF2UUkFSFkU1u125uUJUUZ,"
	echo "             :@kevensun.      ,iY20GOXSUXkSuS2F5XXkUX5SEv."
	echo "         .:i0BMBMBBOOBMUi;,        ,;8PkFP5NkPXkFqPEqqkZu."
	echo "       .rqMqBBMOMMBMBBBM .           @kexianli.S11kFSU5q5"
	echo "     .7BBOi1L1MM8BBBOMBB..,          8kqS52XkkU1Uqkk1kUEJ"
	echo "     .;MBZ;iiMBMBMMOBBBu ,           1OkS1F1X5kPP112F51kU"
}
#主菜单
display_main(){
	echo " 欢迎进入安装程序，本安装脚本运行于centos 6.9 环境,不保证其他版本成功运行!!!"
	echo " 本脚本将会安装Python及其依赖组件,并配置环境变量"
	echo " 文件运行路径:$work_dir, python3安装路径: $install_dir  "
	echo " 请按a,b,c步骤顺序执行"
	echo " 环境变量仅能运行配置一次,配置完环境变量,请手动执行source /etc/profile或者重启!"
	echo "-----------------------------------------------"
	echo "a) 安装依赖组件 "
	echo "b) 安装python"
	echo "c) 配置环境变量"
	echo "d) 退出脚本"
}


# 安装依赖的组件
install_depend(){
	for i in {1..7}  
	do
	ls -l *.rpm |awk '{print $9}' | xargs -n 1 rpm -ivh  
	done  
	echo "-----------------------------rpm install success-----------------------------"
}


# 安装python3
install_python3(){
	tar -zxvf Python-3.6.4.tgz && cd $work_dir/Python-3.6.4
	./configure --prefix=/usr/local/python
	make && make install
}


# 配置环境变量
config_env(){
echo "export PATH=\$PATH:/usr/local/python/bin" >> /etc/profile 
source /etc/profile
echo -e >> ~/.bashrc
cat >> ~/.bashrc <<EOF
alias sudo="sudo env PATH=\$PATH"
EOF
source ~/.bashrc
mkdir ~/.pip && touch ~/.pip/pip.conf
cat >> ~/.pip/pip.conf <<EOF
[global]
timeout = 60
index-url = https://pypi.doubanio.com/simple
[list]
format=columns
EOF

}

main(){
	while true
	do
		clear
		display_logo
		display_main
		read -p "输入选择的的操作:" func
		read -p "确定执行该处理： ["y" or "n"]:" re 
		if [ $re == 'y' ]
		then
			# 执行选定的方法
			sleep 2
			clear
			case "$func" in
				a)
				echo "现在开始安装依赖组件"
				sleep 3
				install_depend
				echo "依赖组件安装成功"
				sleep 3
				clear
				continue
				;;
				b)
				echo "现在开始安装python3"
				sleep 3
				install_python3
				echo "Python3安装成功"
				sleep 3
				clear
				continue
				;;
				c)
				echo "现在开始配置环境变量"
				sleep 3
				config_env
				echo "环境变量配置成功"
				sleep 3
				clear
				continue
				;;
				d)
				echo "退出脚本"
				sleep 3
				clear
				break
				;;
        		*)
				echo "请选择正确的选项"
				sleep 3
				clear
				continue
			esac
		else
			echo "退出操作"
			sleep 3
			clear
			continue
		fi
	done
}
main
