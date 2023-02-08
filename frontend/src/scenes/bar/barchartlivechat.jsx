import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChartStream from "../../components/BarChartStream";
const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart" subtitle="Live Chat Intensity" />
      <Box height="60vh">
        <BarChartStream />
      </Box>
    </Box>
  );
};

export default Bar;
