import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChartBanEvent from "../../components/BarChartBanEvent";
const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Ban Chats" subtitle="Ban Events" />
      <Box height="60vh">
        <BarChartBanEvent />
      </Box>
    </Box>
  );
};

export default Bar;
