import React from 'react';
import {Link,Redirect} from 'react-router-dom';
import '../css/login.css';
import UserService from '../service/user';
import {observer} from 'mobx-react';
import { message } from 'antd';
import 'antd/lib/message/style';
import {inject} from '../service/utils';

const service = new UserService(); 

@inject({service})
@observer
export default class Login extends React.Component{
	handleClick(event){
		event.preventDefault();
		let fm = event.target.form;
		this.props.service.login(
			fm[0].value,fm[1].value
		);
		
	}
	render(){
		if (this.props.service.loggedin){
			return <Redirect to='/' />;
		}
		if (this.props.service.errMsg){
			message.info(this.props.service.errMsg,3,()=>setTimeout(()=>this.props.service.errMsg = ''),1000);
		}
		return (<div className="login-page">
			  <div className="form">
				<form className="login-form">
				  <input type="text" placeholder="邮箱" />
				  <input type="password" placeholder="密码" />
				  <button onClick={this.handleClick.bind(this)}>登录</button>
				  <p className="message">尚未注册? <Link to="/reg">创建一个账号</Link></p>
				</form>
			  </div>
			</div>
		)
	}
}

