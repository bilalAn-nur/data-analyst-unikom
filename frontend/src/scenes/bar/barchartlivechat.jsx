import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChartLiveChart from "../../components/BarChartLiveChat";
const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart" subtitle="Live Chat Intensity" />
      <Box height="60vh">
        <BarChartLiveChart />
      </Box>
    </Box>
  );
};

export default Bar;
