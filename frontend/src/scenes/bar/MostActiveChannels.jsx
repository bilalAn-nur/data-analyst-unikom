import { Box } from "@mui/material";
import Header from "../../components/Header";
import MostActiveChannel from "../../components/MostActiveChannel";

const MostActiveChannels = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart" subtitle="Simple Bar Chart" />
      <Box height="60vh">
        <MostActiveChannel />
      </Box>
    </Box>
  );
};

export default MostActiveChannels;
