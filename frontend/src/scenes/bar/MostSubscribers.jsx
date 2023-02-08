import { Box } from "@mui/material";
import Header from "../../components/Header";
import MostSubscriber from "../../components/MostSubscriber";

const MostSubscribers = () => {
  return (
    <Box m="20px">
      <Header title="Most Subscribers" subtitle="Hololive Group" />
      <Box height="60vh">
        <MostSubscriber />
      </Box>
    </Box>
  );
};

export default MostSubscribers;
