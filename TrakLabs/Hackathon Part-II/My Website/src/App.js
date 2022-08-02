import HomeBody from "./components/HomeBody";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import About from "./components/About";
import Project from "./components/Project";
function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomeBody />} />
          <Route path="/about" element={<About />} />
          <Route path="/project" element={<Project />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
