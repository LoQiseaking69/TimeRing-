import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class RingLaserTimeViewer:
    def __init__(self, wavelength, beam_power, ring_radius, num_detectors, c=299792458, G=6.67430e-11):
        self.wavelength = wavelength
        self.beam_power = beam_power
        self.ring_radius = ring_radius
        self.num_detectors = num_detectors
        self.c = c
        self.G = G

    def calculate_adjusted_pulse_duration(self, obj):
        # Calculate adjusted pulse duration considering gravitational effects
        r = np.linalg.norm(obj.position)
        schwarzschild_radius = 2 * self.G * obj.mass / (self.c ** 2)
        dilation_factor = np.sqrt(1 - (schwarzschild_radius / r))
        return self.wavelength / (self.c * dilation_factor)

    def generate_points(self, obj):
        # Generate points for visualization
        num_points = 100
        points = np.random.uniform(low=obj.min_bound, high=obj.max_bound, size=(num_points, 3))
        return points

    def simulate_experiment(self, scene):
        # Simulate ring laser scanning with gravitational time dilation effects
        adjusted_pulse_durations = []
        for obj in scene.objects:
            adjusted_pulse_duration = self.calculate_adjusted_pulse_duration(obj)
            adjusted_pulse_durations.append(adjusted_pulse_duration)
        return adjusted_pulse_durations

    def visualize_point_cloud(self, point_cloud):
        # Visualize the generated point cloud
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2], c='b', marker='.')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title("Ring Laser Time Viewer Point Cloud")
        plt.show()

if __name__ == "__main__":
    class MassObject:
        def __init__(self, mass, position):
            self.mass = mass
            self.position = position
            # Define bounds for generating points
            self.min_bound = np.array([-1e9, -1e9, -1e9])  # Example: -1e9 for each axis
            self.max_bound = np.array([1e9, 1e9, 1e9])  # Example: 1e9 for each axis

    class Scene:
        def __init__(self, objects):
            self.objects = objects

    # Define multiple massive objects with different positions
    black_hole1 = MassObject(mass=10 ** 36, position=np.array([0, 0, 0]))  # Example: black hole with mass 10^36 kg
    black_hole2 = MassObject(mass=5 * 10 ** 35, position=np.array([1e8, 0, 0]))  # Example: black hole with mass 5*10^35 kg
    black_hole3 = MassObject(mass=2 * 10 ** 35, position=np.array([-1e8, 0, 0]))  # Example: black hole with mass 2*10^35 kg
    scene = Scene(objects=[black_hole1, black_hole2, black_hole3])

    # Set up the parameters for the ring laser time viewer
    time_viewer = RingLaserTimeViewer(
        wavelength=1550e-9,  # Example wavelength
        beam_power=1e-3,  # Example beam power in watts
        ring_radius=1e9,  # Example ring radius
        num_detectors=360,  # Example number of detectors
        c=299792458,
        G=6.67430e-11
    )

    # Simulate the experiment and visualize the results
    adjusted_pulse_durations = time_viewer.simulate_experiment(scene)
    print("Adjusted pulse durations:", adjusted_pulse_durations)

    # Generate and visualize the point cloud
    point_cloud = time_viewer.generate_points(scene.objects[0])  # Generate points for the first object
    time_viewer.visualize_point_cloud(point_cloud)
