<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="19008000">
	<Property Name="varPersistentID:{6F9D0F0A-F7E0-4F0B-9FF4-B7D084F29007}" Type="Ref">/我的电脑/登录.lvlib/用户类型</Property>
	<Property Name="varPersistentID:{7BFF807F-DA9B-456F-ACC6-78D495727563}" Type="Ref">/我的电脑/登录.lvlib/密码</Property>
	<Property Name="varPersistentID:{7E41083C-8878-4217-9B9C-680221E9D897}" Type="Ref">/我的电脑/登录.lvlib/登录用户</Property>
	<Item Name="我的电脑" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">我的电脑/VI服务器</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">我的电脑/VI服务器</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="车牌识别.vi" Type="VI" URL="../车牌识别.vi"/>
		<Item Name="登录.lvlib" Type="Library" URL="../登录.lvlib"/>
		<Item Name="登陆后.vi" Type="VI" URL="../登陆后.vi"/>
		<Item Name="管理员面板.vi" Type="VI" URL="../管理员面板.vi"/>
		<Item Name="历史查询数据.vi" Type="VI" URL="../历史查询数据.vi"/>
		<Item Name="密码重置.vi" Type="VI" URL="../密码重置.vi"/>
		<Item Name="修改密码.vi" Type="VI" URL="../修改密码.vi"/>
		<Item Name="用户登录.vi" Type="VI" URL="../用户登录.vi"/>
		<Item Name="注册用户.vi" Type="VI" URL="../注册用户.vi"/>
		<Item Name="依赖关系" Type="Dependencies">
			<Item Name="user.lib" Type="Folder">
				<Item Name="ADO Connection Close.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/Connection/ADO Connection Close.vi"/>
				<Item Name="ADO Connection Create.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/Connection/ADO Connection Create.vi"/>
				<Item Name="ADO Connection Destroy.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/Connection/ADO Connection Destroy.vi"/>
				<Item Name="ADO Connection Execute.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/Connection/ADO Connection Execute.vi"/>
				<Item Name="ADO Connection Open.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/Connection/ADO Connection Open.vi"/>
				<Item Name="ADO Recordset Destroy.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/Recordset/ADO Recordset Destroy.vi"/>
				<Item Name="ADO Recordset GetString.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/Recordset/ADO Recordset GetString.vi"/>
				<Item Name="SQL Execute.vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/SQL Execute.vi"/>
				<Item Name="SQL Fetch Data (GetString).vi" Type="VI" URL="/&lt;userlib&gt;/LabSQL ADO functions/SQL Fetch Data (GetString).vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
				<Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Create"/>
				<Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
				<Item Name="IMAQ ReadFile 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ ReadFile 2"/>
				<Item Name="Set Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Busy.vi"/>
				<Item Name="Set Cursor (Cursor ID).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor (Cursor ID).vi"/>
				<Item Name="Set Cursor (Icon Pict).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor (Icon Pict).vi"/>
				<Item Name="Set Cursor.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="subFile Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/FileDialogBlock.llb/subFile Dialog.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Unset Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Unset Busy.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
			</Item>
			<Item Name="nivision.dll" Type="Document" URL="nivision.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="程序生成规范" Type="Build"/>
	</Item>
</Project>
