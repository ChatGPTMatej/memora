import "./Preloader.css";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";

export default function Preloader({ onFinish }) {
  const [startZoom, setStartZoom] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setStartZoom(true), 1000);
    const finishTimer = setTimeout(onFinish, 2600);

    return () => {
      clearTimeout(timer);
      clearTimeout(finishTimer);
    };
  }, [onFinish]);

  return (
    <motion.div
      className="preloader"
      initial={{ opacity: 1 }}
      animate={{ opacity: startZoom ? 0 : 1 }}
      transition={{ duration: 0.8, ease: "easeInOut" }}
    >
      <motion.h1
        className="logo"
        initial={{ scale: 1 }}
        animate={{ scale: startZoom ? 20 : 1 }}
        transition={{ duration: 1.4, ease: "easeInOut" }}
      >
        MEMORA
      </motion.h1>
    </motion.div>
  );
}
