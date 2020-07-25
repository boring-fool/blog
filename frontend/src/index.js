import React from 'react';
import ReactDom from 'react-dom';
import Login from './component/login';
import Reg from './component/reg';
import {Route,Link,BrowserRouter as Router} from 'react-router-dom';
import {Layout,Menu,Icon} from 'antd';
import Pub from './component/pub';
import  L from './component/list';
import Post from './component/post';
import 'antd/lib/layout/style';
import 'antd/lib/menu/style';
import 'antd/lib/icon/style';

const {Header,Content,Footer} = Layout;

const Home = () =>(
	<div>
		<h2>Home</h2>
	</div>
);
const About = () =>(
	<div>
		<h2>About</h2>
	</div>
);
const App = () => (
	<Router>
		<Layout>
		  <Header>
			<Menu mode = "horizontal">
				<Menu.Item key = "home"><Link to ="/"><Icon type="home" />主页</Link></Menu.Item>
				<Menu.Item key = "login"><Link to ="/login"><Icon type="login" />登录</Link></Menu.Item>
				<Menu.Item key = "reg"><Link to ="/reg">注册</Link></Menu.Item>
				<Menu.Item key = "pub"><Link to = "/pub">发布</Link></Menu.Item>
				<Menu.Item key = "list"><Link to ="/list"><Icon type="bars" />文章列表</Link></Menu.Item>
				<Menu.Item key = "about"><Link to ="/about">关于</Link></Menu.Item>
			</Menu>
		  </Header>
		  <Content style = {{padding : '8px 50px'}}>
			<div style ={{background : '#fff',padding : 24,minHeight : 280}}>
			<Route path="/about" component={About} />
			<Route path="/login" component={Login} />
			<Route path="/reg" component={Reg} />
			<Route path="/pub" component={Pub} />
			<Route path="/list" component={L} />
			<Route exact path="/post/:id" component={Post} />
			<Route exact path = "/" component={Home} />
		</div>
		<Footer style = {{textAlign:'center'}}>
		 博客@2020
		</Footer>
		</Content>
		</Layout>
	</Router>
);
ReactDom.render(<App />,document.getElementById('root'));