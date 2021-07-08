import * as React from 'react';
import { DataGrid, GridToolbar } from '@material-ui/data-grid';
import axios from 'axios';


var columns = [
    { 'field': 'id', 'headerName': 'ID' ,'flex': 0.3},
    { 'field': 'stockcode', 'headerName': '股票名称' ,'flex': 1},
    { 'field': 'price', 'headerName': '现价' ,'flex': 1},
    { 'field': 'hand', 'headerName': '持有','flex': 1 },
    { 'field': 'canuse', 'headerName': '可用','flex': 1}
];

var rowss = [];

export default function Acountview() {
    //const [data, setDatas] = React.useState({'test':'test'});
    const [rowsss, setDatas] = React.useState(rowss);
    const [colsss, setCols] = React.useState(columns);
    const timer = React.useRef();

    const reflash_data=() => {
      axios.post('/main/account').then( response =>{
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
