import * as React from 'react';
import { DataGrid, GridToolbar } from '@material-ui/data-grid';
import axios from 'axios';


var columns = [
    { 'field': 'code', 'headerName': '基金代码' ,'flex': 1},
    { 'field': 'name', 'headerName': '基金名称' ,'flex': 1},
    { 'field': 'price', 'headerName': '市值' ,'flex': 1},
    { 'field': 'profit', 'headerName': '涨跌价','flex': 1 },
    { 'field': 'rate', 'headerName': '涨跌幅','flex': 1},
    { 'field': 'speed', 'headerName': '涨跌速','flex': 1}
];

var rowss = [];

export default function ETFView() {
    //const [data, setDatas] = React.useState({'test':'test'});
    const [rowsss, setDatas] = React.useState(rowss);
    const [colsss, setCols] = React.useState(columns);
    const timer = React.useRef();

    const reflash_data=() => {
      axios.post('/main/etf').then( response =>{
          //console.log(response.data)
          var vdata=response.data
          columns=vdata.cols;
          rowss=vdata.rows;
          setDatas(vdata.rows);
          setCols(vdata.cols);
          //setDatas({data:vdata});
         
      });
      
  }

  if(rowsss.length==0) {
    reflash_data();
  }

    if(!timer.current)
    {
      timer.current = setInterval(reflash_data,5000);
    }


  return (
    <div style={{ height: 500, width: '100%'  }}>
      <DataGrid rows={rowsss} columns={colsss} disableColumnMenu={true}  components={{
          Toolbar: GridToolbar,
        }} />
    </div>
  );
}
