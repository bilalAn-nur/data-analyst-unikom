import { Avatar, Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import Header from "../../components/Header";
import { useTheme } from "@mui/material";
import React, { useState, useEffect } from "react";
import axios from "axios";

const Contacts = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("/api").then((res) => setData(res.data));
  }, []);

  const columns = [
    { field: "channelId", headerName: "Link", flex: 1},
    { field: "name", headerName: "Channel", flex: 1 },
    // { field: "englishName", headerName: "Nama ", flex: 1, cellClassName: "name-column-cell"},
    {
      field: "affiliation",
      headerName: "Agensi",
      headerAlign: "left",
      align: "left",
    },
    { field: "group", headerName: "Grup", flex: 1 },
    { field: "subscriptionCount", headerName: "Subscriber", flex: 1 },
    { field: "videoCount", headerName: "Video", flex: 1 },
    {
      field: "photo",
      headerName: "Profile",
      renderCell: (params) => <Avatar src={params.row.photo} />,
      sortable: false,
    },
  ];

  return (
    <Box m="20px">
      <Header
        title="V-TUBER"
        subtitle="List V-Tuber"
      />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
          "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
          },
        }}
      >
        <DataGrid
          rows={data}
          columns={columns}
          components={{ Toolbar: GridToolbar }}
          getRowId={(row) => row.channelId}
        />
      </Box>
    </Box>
  );
};

export default Contacts;
