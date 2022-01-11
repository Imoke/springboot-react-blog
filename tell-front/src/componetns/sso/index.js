import React, { Component } from 'react';
import {ssoAsync} from '../../redux/user/action';
import {connect} from 'react-redux';
/**
 * @Author: miansen
 * @Date: 2018/11/28
 * @description: 登录窗口
 */
class Sso  extends Component{

      //在渲染前调用
      componentWillMount(){
        const query = this.props.location.search.substr(1);
        const arr = query.split('&');
        function key_value_obj() {
            this.key = []; //键数组
            this.keyvalue = []; //值数组
            this.counter = 0; //计数器，用于存储数据数量
        } //数据存储方式-->顺序存储，线性表
        var obj = new key_value_obj();
        //创建对象

        function deal_with_key_value(obj, key_and_value) {
            for (var i = 0; i < key_and_value.length; i++) {
                var pos = key_and_value[i].split('=');
                obj.key[i] = pos[0];
                obj.keyvalue[i] = pos[1];
                obj.counter++;
            } //遍历location.search中每一个元素
        }
        deal_with_key_value(obj, arr); //调用
        this.props.ssoAsync({url: "/sso", 
            token: obj.keyvalue[0],
            time: obj.keyvalue[1],
            username: obj.keyvalue[2],
            page: obj.keyvalue[3],
        });
    }

    render() {
        return ('');
    }
}

export default connect(
    state => ({
        state: state
    }),
    {ssoAsync: ssoAsync}
)(Sso);