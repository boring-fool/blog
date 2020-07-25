import axios from 'axios';
import {observable} from 'mobx';
import store from 'store';

export default class PostService{
	constructor(){
		this.axios = axios.create({
			baseURL : '/api/post/'
		});
	}
	@observable msg = "";
	@observable posts = [];
	@observable pagination = {page:1,size:20,pages:0,count:0}
	getJwt(){
		return store.get('token',null)
	}
	pub(title,content){
		console.log(title);
		this.axios.post('pub',{
			title,
			content
		},{headers:{'Jwt':this.getJwt()}}).then(
			response=>{
				this.msg = "提交成功";
			}
		).catch(
			error=>{
				this.msg='登陆失败';
			}
		)
	}
	
	list(search){
		this.axios.get(search).then(
		response=>{
			this.posts = response.data.posts;
			this.pagination = response.data.pagination;
		}
		).catch(
		error=>{
			this.msg = "文章加载失败";
		}
		)
	}
	
	
}