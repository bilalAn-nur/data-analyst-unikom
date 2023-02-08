import { ColorModeContext, useMode } from "./theme";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { Routes, Route } from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
import Dashboard from "./scenes/dashboard";
import MostActiveChannels from "./scenes/bar/MostActiveChannels";
import Channels from "./scenes/channel";
import MostSubscribers from "./scenes/bar/MostSubscribers";
import BarStream from "./scenes/bar/barchartstream";
import BarSubsPerGroup from "./scenes/bar/SubsGroup";
import MostLiveChats from "./scenes/bar/MostLiveChats";
import BarBanEvent from "./scenes/bar/barchartbanevent";
import Pie from "./scenes/pie";
import Geography from "./scenes/geography";

function App() {
  const [theme, colorMode] = useMode();

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar />
          <main className="content">
            <Topbar />
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/channels" element={<Channels />} />
              <Route path="/most_subscribers" element={<MostSubscribers />} />
              <Route
                path="/most_active_channels"
                element={<MostActiveChannels />}
              />
              <Route path="/most_live_chat" element={<MostLiveChats />} />
              <Route path="/barstream" element={<BarStream />} />
              <Route path="/subs_group" element={<BarSubsPerGroup />} />
              <Route path="/barbanevent" element={<BarBanEvent />} />
              <Route path="/pie" element={<Pie />} />
              <Route path="/geography" element={<Geography />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
