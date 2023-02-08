import { Box, Button, IconButton, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";
import { mockTransactions } from "../../data/mockData";
import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import EmailIcon from "@mui/icons-material/Email";
import PointOfSaleIcon from "@mui/icons-material/PointOfSale";
import PersonAddIcon from "@mui/icons-material/PersonAdd";
import TrafficIcon from "@mui/icons-material/Traffic";
import Header from "../../components/Header";
import LineChart from "../../components/LineChart";
import GeographyChart from "../../components/GeographyChart";
import MostSubscribers from "../../components/MostSubscriber";
import StatBox from "../../components/StatBox";
import ProgressCircle from "../../components/ProgressCircle";
import axios from "axios";
import { useState, useEffect } from "react";

const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [data, setData] = useState([]);
  useEffect(() => {
    axios.get("/api").then((res) => setData(res.data));
  }, []);
  const totalSubscriptions = data.reduce(
    (acc, item) => acc + item.subscriptionCount,
    0
  );

  return (
    <Box m="20px">
      {/* HEADER */}
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Header
          title="KELOMPOK DATA ANALIYST V-TUBER"
          subtitle="YouTube adalah sebuah situs web berbagi video yang memungkinkan pengguna mengunggah, menonton, dan berbagi video. Youtube diisi oleh seorang pengonten yang disebut juga sebagai Youtuber.

          YouTuber merupakan videografer yang membuat video untuk diunggah di YouTube. Trend saat ini Youtube tidak hanya diisi oleh Youtuber itu sendiri namun diwakili oleh avatar digital atau disebut juga sebagai V-Tuber.
          
          Avatar digital sebagai V-Tuber dihasilkan oleh grafik komputer. V-Tuber merupakan karakter fiksi 2D maupun 3D yang menjalankan kanal YouTube. V-Tuber berperan sebagai penghibur daring yang menggunakan avatar yang dibuat oleh komputer.
          
          Semakin tingginya pasar V-Tuber berdampak pada makin banyaknya peminat sebagai V-Tuber, baik talent baru maupun beralih dari YouTuber."
        />
      </Box>
    </Box>
  );
};

export default Dashboard;
