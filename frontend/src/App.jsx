import { useState } from "react";
import { Routes, Route, Link } from "react-router-dom";
import { AnimatePresence } from "framer-motion";

import Preloader from "./components/Preloader";
import AddPerson from "./components/AddPerson";
import Button from "./components/button";

const Home = () => {
  return (
    <div className="home">
      <Link to="/admin" className="admin-link">
        <Button>ADMIN</Button>
      </Link>

      <div className="hero">
        <h1>MEMORA</h1>
        <p>Digital memory. Clean future.</p>
      </div>
    </div>
  );
};

const App = () => {
  const [showIntro, setShowIntro] = useState(true);

  return (
    <>
      {showIntro && <Preloader onFinish={() => setShowIntro(false)} />}

      {!showIntro && (
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/admin" element={<AddPerson />} />
        </Routes>
      )}
    </>
  );
};

export default App;
