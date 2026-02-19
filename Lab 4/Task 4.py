power_grid = {
    'main_box': ['zone_a', 'zone_b'],
    'zone_a': ['switch_1', 'switch_2'],
    'zone_b': ['breaker_101'],
    'switch_1': [],
    'switch_2': [],
    'breaker_101': []
}
def depth_limited_search(current, target, limit):
    print("inspecting:", current)

    if current == target:
        return True

    if limit == 0:
        return False

    for neighbor in power_grid.get(current, []):
        found = depth_limited_search(neighbor, target, limit - 1)
        if found:
            return True

    return False

def iterative_deepening(start_node, target_node, max_level):
    level = 0

    while level <= max_level:
        print(f"\nChecking Depth {level}...")

        if depth_limited_search(start_node, target_node, level):
            print("\nBreaker_101 located! Power restored successfully.")
            return

        level += 1
    print("Target breaker not detected within depth range.")

iterative_deepening('main_box', 'breaker_101', 2)
