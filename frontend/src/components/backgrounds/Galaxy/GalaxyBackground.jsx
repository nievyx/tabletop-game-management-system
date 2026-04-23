import Galaxy from "./Galaxy/Galaxy";

function GalaxyBackground() {
    return (
        <div className="background-layer">
            <Galaxy
                mouseRepulsion={false}
                mouseInteraction
                density={2.6}
                glowIntensity={0.2}
                saturation={0}
                hueShift={140}
                twinkleIntensity={0.4}
                rotationSpeed={0.05}
                repulsionStrength={2}
                autoCenterRepulsion={0}
                starSpeed={0.2}
                speed={1}
            />
        </div>
    );
}

export default GalaxyBackground;