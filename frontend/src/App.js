import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Switch, Route,Redirect } from 'react-router-dom';
import PersistentDrawerLeft from './component/drawer';
import LoginDialog from './component/login';
import Acountview from './component/accounter';
function App() {
  return (
    <div className="App">

      {/* <Acountview/> */}
      <BrowserRouter>
        <Switch>
        <Redirect exact from='/' to='/main' />
        <Route path="/users/login" component={LoginDialog.bind({open:true})} />
        <Route path="/main" component={PersistentDrawerLeft}/>
        </Switch>
      </BrowserRouter>
      {/* <header className="App-header">


        
        
      </header> */}
    </div>
  );
}

export default App;
