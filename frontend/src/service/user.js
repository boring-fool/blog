import axios from 'axios';
import store from 'store';
import {observable} from 'mobx';

//过期插件
store.addPlugin(require('store/plugins/expire'));
export default class UserService{
	@observable errMsg = '';
	@observable loggedin = false; //被观察者
	login(email,password){
		axios.post('/api/user/login',{
			email:email,
			password:password
		})
	.then(
		response=>{
			console.log(response);
			console.log(response.data);
			store.set('token',response.data.token,(new Date()).getTime()+(8*3600*1000));
			this.loggedin = true
		}
	).catch(
	error=>{
		console.log(error);
		this.errMsg = '登录失败';
	})
	}
	reg(name,email,password){
		axios.post('/api/user/reg',{
			email:email,
			password:password,
			name:name
		}).then(
		response =>{
			console.log(response.data);
			console.log(response.status);
			store.set('token',
			response.data.token,
			(new Date()).getTime() + (8*3600*1000)
			);
			this.loggedin = true 
		}
		).catch(
			error=>{
				console.log(error)
				this.errMsg = '注册失败';
			}
		)
	}
}