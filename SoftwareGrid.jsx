import { useState } from "react";

const softwareIcons = [
  {
    name: "Photoshop",
    abbr: "Ps",
    color: "#31A8FF",
    bg: "#001E36",
    level: 75,
  },
  {
    name: "Premiere Pro",
    abbr: "Pr",
    color: "#9999FF",
    bg: "#00005B",
    level: 75,
  },
  {
    name: "Illustrator",
    abbr: "Ai",
    color: "#FF9A00",
    bg: "#1C0A00",
    level: 90,
  },
  {
    name: "After Effects",
    abbr: "Ae",
    color: "#9999FF",
    bg: "#00005B",
    level: 20,
  },
  {
    name: "CapCut",
    abbr: "CC",
    color: "#FFFFFF",
    bg: "#000000",
    level: 90,
  },
  {
    name: "Notion",
    abbr: "N",
    color: "#FFFFFF",
    bg: "#1A1A1A",
    level: 90,
  },
];

const SoftwareIcon = ({ icon }) => {
  const [hovered, setHovered] = useState(false);

  const orbitIcons = softwareIcons.filter((i) => i.abbr !== icon.abbr);

  return (
    <div
      style={{
        position: "relative",
        width: 120,
        height: 120,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        cursor: "pointer",
      }}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
    >
      {/* Orbit ring */}
      <div
        style={{
          position: "absolute",
          width: 110,
          height: 110,
          borderRadius: "50%",
          border: `1px solid rgba(220,20,20,${hovered ? 0.6 : 0})`,
          boxShadow: hovered ? "0 0 20px rgba(220,20,20,0.3)" : "none",
          transition: "all 0.4s ease",
          animation: hovered ? "spin 2s linear infinite" : "none",
        }}
      />

      {/* Orbiting mini icons */}
      {orbitIcons.map((orb, i) => {
        const angle = (360 / orbitIcons.length) * i;
        const rad = (angle * Math.PI) / 180;
        const radius = 55;
        const x = Math.cos(rad) * radius;
        const y = Math.sin(rad) * radius;
        return (
          <div
            key={orb.abbr}
            style={{
              position: "absolute",
              width: 22,
              height: 22,
              borderRadius: 4,
              background: orb.bg,
              border: `1px solid ${orb.color}44`,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 8,
              fontWeight: 900,
              color: orb.color,
              fontFamily: "monospace",
              transform: hovered
                ? `translate(${x}px, ${y}px) scale(1)`
                : `translate(0px, 0px) scale(0)`,
              opacity: hovered ? 1 : 0,
              transition: `all 0.5s cubic-bezier(0.34,1.56,0.64,1) ${i * 0.06}s`,
              zIndex: 10,
              boxShadow: hovered ? `0 0 8px ${orb.color}66` : "none",
            }}
          >
            {orb.abbr}
          </div>
        );
      })}

      {/* Main icon */}
      <div
        style={{
          width: 72,
          height: 72,
          borderRadius: 14,
          background: icon.bg,
          border: `2px solid ${icon.color}`,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontSize: 22,
          fontWeight: 900,
          color: icon.color,
          fontFamily: "monospace",
          boxShadow: hovered
            ? `0 0 30px ${icon.color}88, 0 0 60px ${icon.color}44, inset 0 0 20px ${icon.color}22`
            : `0 0 15px ${icon.color}44`,
          transform: hovered ? "scale(1.12)" : "scale(1)",
          transition: "all 0.35s cubic-bezier(0.34,1.56,0.64,1)",
          zIndex: 20,
          position: "relative",
        }}
      >
        {icon.abbr}

        {/* Corner dots like the image */}
        {[[-1, -1], [1, -1], [-1, 1], [1, 1]].map(([dx, dy], i) => (
          <div
            key={i}
            style={{
              position: "absolute",
              width: 4,
              height: 4,
              borderRadius: "50%",
              background: "#cc1111",
              top: dy === -1 ? -8 : "auto",
              bottom: dy === 1 ? -8 : "auto",
              left: dx === -1 ? -8 : "auto",
              right: dx === 1 ? -8 : "auto",
              boxShadow: "0 0 6px #cc1111",
            }}
          />
        ))}
      </div>

      {/* Level bar below */}
      <div
        style={{
          position: "absolute",
          bottom: -18,
          left: "50%",
          transform: "translateX(-50%)",
          width: 72,
        }}
      >
        <div
          style={{
            height: 3,
            background: "#1a0000",
            borderRadius: 2,
            overflow: "hidden",
            border: "1px solid #cc111133",
          }}
        >
          <div
            style={{
              height: "100%",
              width: `${icon.level}%`,
              background: `linear-gradient(90deg, #cc1111, #ff4444)`,
              borderRadius: 2,
              boxShadow: "0 0 6px #cc1111",
              transition: "width 1s ease 0.3s",
            }}
          />
        </div>
        <div
          style={{
            textAlign: "center",
            fontSize: 9,
            color: "#888",
            marginTop: 2,
            fontFamily: "monospace",
            letterSpacing: 1,
          }}
        >
          {icon.level}%
        </div>
      </div>
    </div>
  );
};

export default function SoftwareGrid() {
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#0a0a0a",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 40,
        fontFamily: "monospace",
      }}
    >
      <style>{`
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
        @keyframes pulse-red {
          0%, 100% { opacity: 0.4; }
          50% { opacity: 1; }
        }
      `}</style>

      {/* Grid dots background */}
      <div
        style={{
          position: "fixed",
          inset: 0,
          backgroundImage:
            "radial-gradient(circle, #cc111122 1px, transparent 1px)",
          backgroundSize: "30px 30px",
          pointerEvents: "none",
        }}
      />

      <div
        style={{
          color: "#cc1111",
          fontSize: 11,
          letterSpacing: 4,
          textTransform: "uppercase",
          marginBottom: 8,
          animation: "pulse-red 2s ease infinite",
        }}
      >
        ◆ SOFTWARE SKILLS ◆
      </div>
      <h1
        style={{
          color: "white",
          fontSize: 28,
          fontWeight: 900,
          letterSpacing: 6,
          marginBottom: 60,
          textTransform: "uppercase",
          textShadow: "0 0 30px rgba(220,20,20,0.5)",
        }}
      >
        VALENTIN SANCHEZ
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, 140px)",
          gap: "60px 40px",
          justifyItems: "center",
        }}
      >
        {softwareIcons.map((icon) => (
          <SoftwareIcon key={icon.abbr} icon={icon} />
        ))}
      </div>

      <div
        style={{
          marginTop: 80,
          color: "#444",
          fontSize: 10,
          letterSpacing: 3,
          textTransform: "uppercase",
        }}
      >
        HOVER PARA ACTIVAR ↑
      </div>
    </div>
  );
}
