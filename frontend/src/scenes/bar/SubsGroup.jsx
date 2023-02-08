import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChartSubsPerGroup from "../../components/BarChartSubsPerGroup";
const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart" subtitle="Most Subscribed Channels per Group" />
      <Box height="60vh">
        <BarChartSubsPerGroup />
      </Box>
    </Box>
  );
};

export default Bar;
