import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChartLoro from "../../components/BarChartLoro";
const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart" subtitle="Simple Bar Chart" />
      <Box height="60vh">
        <BarChartLoro />
      </Box>
    </Box>
  );
};

export default Bar;
