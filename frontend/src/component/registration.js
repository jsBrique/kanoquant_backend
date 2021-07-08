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




export default function RegistrationDialog() {
  const [open, setOpen] = React.useState(true);
  
  const [loginform,setLogin ] = React.useState({
    username:"",
    password:"",
    rememberme:false
  });

  var loginformtmp=loginform;
  var inputChange = (e) =>
  {
    loginformtmp[e.target.id]=e.target.value;
    setLogin(loginformtmp);

  };

  const LoginFormCheck=()=>{
    axios.post('/Registration', {loginform:loginform});
  };

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    
    setOpen(false);
  };

  return (
    <div>
      <Button variant="outlined" color="primary" onClick={handleClickOpen}>
        Registration
      </Button>
      <Dialog open={open}  aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">注册</DialogTitle>
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
          />
          <TextField
            onChange={inputChange}
            autoFocus
            margin="dense"
            id="password"
            label="密码"
            data-id="password"
            type="password"
            autoComplete="current-password"
            fullWidth
          />

        {/* <FormControlLabel value="tips" label={loginform['username']+'\n'+loginform['password']}/> */}
        {/* <Paper elevation={3} >{"content="+loginform['username']+'\n'+loginform['password']}</Paper> */}
        </DialogContent>
        <DialogActions>
     
          <Button size="large" onClick={LoginFormCheck} variant="contained" color="primary">
            {"注册"}
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}