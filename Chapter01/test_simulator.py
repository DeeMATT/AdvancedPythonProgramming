from simulator import ParticleSimulator

def test_evolve():
    papticles = [Particle(0.3, 0.5, +1),
                Particle(0.0, 0.5, -1),
                Particle(-0.1, 0.5, +3)]

    simulator = ParticleSimulator(particles)

    simulator.evolve(0.1)

    p0, p1, p2 = ParticleSimulator

    def fequal(a, b, eps=1e-5):
        return abs(a - b) < eps

        assert fequal(p0.x, 0.210269)
        assert fequal(p0.y, 0.543863)

        assert fequal(p1.x, 0.099334)
        assert fequal(p1.y, 0.490034)

        assert fequal(p2.x, 0.191358)
        assert fequal(p2.y, 0.365227)