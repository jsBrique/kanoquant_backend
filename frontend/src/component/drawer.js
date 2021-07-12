import React from 'react';
import clsx from 'clsx';

import { makeStyles, useTheme } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import axios from 'axios';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ShowChartIcon from '@material-ui/icons/ShowChart';
import AccountBalanceWalletIcon from '@material-ui/icons/AccountBalanceWallet';
import ThumbUpIcon from '@material-ui/icons/ThumbUp';
import AccountBoxIcon from '@material-ui/icons/AccountBox';
import MonetizationOnIcon from '@material-ui/icons/MonetizationOn';
import GitHubIcon from '@material-ui/icons/GitHub';
import RedeemIcon from '@material-ui/icons/Redeem';
import AccountCircle from '@material-ui/icons/AccountCircle';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Acountview from './accounter';
import ETFView from './ETF';
import { Redirect,useHistory,withRouter   } from 'react-router-dom';
const drawerWidth = 180;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    
  },
  appBar: {
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  // menuButton: {
  //   marginRight: theme.spacing(2),
  // },
  userButton:{

    float: 'right',
  },
  hide: {
    display: 'none',
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  drawerHeader: {
    display: 'flex',
    alignItems: 'center',
    padding: theme.spacing(0, 1),
    // necessary for content to be below app bar
    ...theme.mixins.toolbar,
    justifyContent: 'flex-end',
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginLeft: -drawerWidth,
  },
  usermenu:{
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
  },
  contentShift: {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
    marginLeft: 0,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));



function testuser()
{

  axios.post('/users/test').then(response =>{
    console.log(response.data);
  });

}

export default function PersistentDrawerLeft(props) {
  const historys=useHistory();
  const classes = useStyles();
  const theme = useTheme();
  const [open, setOpen] = React.useState(false);
  const [pageid, setPage] = React.useState(0);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [useropen, setUserOpen] = React.useState(Boolean(anchorEl));
  const [username, setUsername] = React.useState("Unknow");

  var logoutfunc=()=>
  {
    historys.push('/users/login');
    axios.post('/users/logout');
    console.log('logout');
  }


var btnconf=[
    {id:0,name:'趋势量化',icon:<ShowChartIcon/>,select:true,component:<ETFView/>},
    {id:1,name:'仓位管理',icon:<AccountBalanceWalletIcon/>,select:false,component:<Acountview/>},
    {id:2,name:'收益分析',icon:<ThumbUpIcon/>,select:false,component:'收益分析-施工中'},
    {id:3,name:'可转债',icon:<MonetizationOnIcon/>,select:false,component:'可转债-施工中'}
    
];
const otherconf=[
  {id:0,name:'开源仓库',icon:<GitHubIcon/>},
  {id:1,name:'捐助渠道',icon:<RedeemIcon/>},
];
//设置默认当前选中
const [current, setcurrent] = React.useState(0);
//点击tab栏切换事件
const clickevent = React.useCallback((item, key) => {
  setcurrent(key);
  console.log(btnconf[key]['name'])
});

const checkuser=()=>{
  
  axios.get('/users/check').then(response =>{
    //var loginname=response.data.username;
    setUsername(response.data.username)
  });

}

const handleUserOpen=(event)=>{
  setAnchorEl(event.currentTarget);
  var u=checkuser();
  //setUsername(u);
  setUserOpen(true);
}
const handleUserClose=()=>{
  setUserOpen(false);
}

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  var btntext=[];
  for(var i=0;i<btnconf.length;i++)
  {
    btntext.push(btnconf[i]['name']);
    if(current==i)
    {
      btnconf[i]['select']=true;
    }else
    {
      btnconf[i]['select']=false;
    }
  }
  var othertext=[];
  for(var i=0;i<otherconf.length;i++)
  {
    othertext.push(otherconf[i]['name']);

  }
  // console.log(btnconf);
//   console.log(btnconf);
  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar
        position="fixed"
        className={clsx(classes.appBar, {
          [classes.appBarShift]: open,
        })}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            className={clsx(classes.menuButton, open && classes.hide)}
          >
            <MenuIcon />

          </IconButton>
         
          <Typography className={classes.title} variant="h6" noWrap>
            {'鹿角量化'}
          </Typography>
          <div>
          <IconButton 
          color="inherit"
          aria-haspopup="true"
          aria-label="用户"
          aria-controls="menu-appbar"
          onClick={handleUserOpen}
          >
            <AccountCircle />
          </IconButton>
          <Menu
          open={useropen}
          onClose={handleUserClose}
          anchorEl={anchorEl}
          anchorOrigin={{
            vertical: 'top',
            horizontal: 'right',
          }}
          transformOrigin={{
            vertical: 'top',
            horizontal: 'right',
          }}
          >
            <MenuItem>{(username=='Unknow')?'登陆':username}</MenuItem>
            <MenuItem onClick={testuser} >路由测试</MenuItem>
            <MenuItem onClick={logoutfunc} >退出登陆</MenuItem>
          </Menu>
          </div>
        </Toolbar>
      
      </AppBar>
      <Drawer
        className={classes.drawer}
        variant="persistent"
        anchor="left"
        open={open}
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <div className={classes.drawerHeader}>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
          </IconButton>
        </div>
        <Divider />
        
        <List>
          {btntext.map((text, index) => (
            <ListItem button key={text} selected={btnconf[index]['select']} onClick={clickevent.bind(null, text, btnconf[index]['id'])}>
              <ListItemIcon>{btnconf[index]['icon']}</ListItemIcon>
              <ListItemText primary={text} />
            
            </ListItem>
          ))}
        </List>
        <Divider />
        <List>
          {othertext.map((text, index) => (
            <ListItem button key={text}>
              <ListItemIcon>{otherconf[index]['icon']}</ListItemIcon>
              <ListItemText primary={text} />
            </ListItem>
          ))}
        </List>
      </Drawer>
      
      <main
        className={clsx(classes.content, {
          [classes.contentShift]: open,
        })}
      >
        
        <div className={classes.drawerHeader} />
        <div>{btnconf[current].component}</div>
        
      </main>
      
    </div>
    
  );
}