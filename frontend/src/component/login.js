import React from 'react';
import Button from '@material-ui/core/Button';
import Checkbox from '@material-ui/core/Checkbox';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';
import Snackbar from '@material-ui/core/Snackbar';
import Alert from '@material-ui/lab/Alert';
import backgroundimg from '../resources/background.jpg';
import './login.css';
import { Redirect,useHistory ,withRouter   } from 'react-router-dom';
// import MuiAlert from '@material-ui/lab/Alert';
import { makeStyles } from '@material-ui/core/styles';

// function Alert(props) {
//   return <MuiAlert elevation={6} variant="filled" {...props} />;
// }



export default function LoginDialog(props) {
  const history = useHistory();
  const [open, setOpen] = React.useState(true);
  const [loginerror, setError] = React.useState(false);
  const [usernameCheck, setUsername] = React.useState('Unknow');
  const [tipsopen, setTipsopen] = React.useState(false);
  const [loginstate,setLoginState] = React.useState(false);
  const [logincheckstate,setCheckState] = React.useState(false);
  const [loginform,setLogin ] = React.useState({
    username:"",
    password:"",
    rememberme:false
  });
  const tipsClose = () => {
    
    setTipsopen(false);
  };

  const tipsOpen = () => {
    
    setTipsopen(true);
  };
  if (props.open==true && open==false) {
    setOpen(true);
  }
  if (props.open==false && open==true) {
    setOpen(false);
  }
  
  const checkuser=()=>{
  
    axios.get('/users/check').then(response =>{
      //var loginname=response.data.username;
      setUsername(response.data.username)
    });
    if(usernameCheck!='Unknow')
    {
      setOpen(false);
      setLoginState(true);
    }
  }
  if(logincheckstate==false)
  {
    checkuser();
    setCheckState(true);
  }
  
  var loginformtmp=loginform;
  var inputChange = (e) =>
  {
    loginformtmp[e.target.id]=e.target.value;
    setLogin(loginformtmp);
    
  };

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    
    setOpen(false);
  };
  const LoginFormCheck=()=>{
    axios.post('/users/logincheck', loginform).then(response => {
      console.log('/users/logincheck', response.data);
      if (response.data.Login==true)
      {

        setOpen(false);
        setTipsopen(true);
        //Redirect(to='/main/');
        history.push('/main');
        //this.props.history.push("/main");
      }else
      {
        setError(true);
      }
  });

  };
  const RegistrationFormCheck=()=>{
    axios.post('/registration', loginform);
  };
  // if(loginstate==false)
  // {
    return (
      
      <div >
          <img class="backgroundimg" src={backgroundimg}   ></img>
      
        <Dialog open={open}  aria-labelledby="form-dialog-title">
          
          <DialogTitle id="form-dialog-title">登陆</DialogTitle>
          <DialogContent>
  
            <TextField
              onChange={inputChange}
              autoFocus
              margin="dense"
              id="username"
              label="账号"
              data-id="username"
              // type="email"
              fullWidth
              error={loginerror}
            />
            <TextField
              error={loginerror}
              onChange={inputChange}
              autoFocus
              margin="dense"
              id="password"
              label="密码"
              data-id="password"
              type="password"
              autoComplete="current-password"
              fullWidth
              helperText={
                (loginerror==true)?"账号或密码错误":""
           
              }
            />
          <FormControlLabel
            value="end"
            control={<Checkbox color="primary" />}
            label={"记住我"}
          //   labelPlacement="end"
          />
          {/* <FormControlLabel value="tips" label={loginform['username']+'\n'+loginform['password']}/> */}
          {/* <Paper elevation={3} >{"content="+loginform['username']+'\n'+loginform['password']}</Paper> */}
          </DialogContent>
          <DialogActions>
            {/* <Button size="large" onClick={RegistrationFormCheck} variant="contained" color="secondary"> 
              注册
              </Button> */}
            <Button size="large" onClick={LoginFormCheck} variant="contained" color="primary">
              {"登陆"}
            </Button>
  
          </DialogActions>
        </Dialog>
        <Snackbar open={tipsopen} autoHideDuration={3000} onClose={tipsClose}>
          <Alert onClose={tipsClose} severity="success">
            登陆成功
          </Alert>
        </Snackbar>
   
      </div>
    );
 

}