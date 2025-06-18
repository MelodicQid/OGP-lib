if __name__ == "__main__":
    from observer import Observer
    from generator import generate_key_path
    from visualizer import visualize_observer_chain

    O1 = Observer("psi")
    O2 = Observer(O1)
    O3 = Observer(O2)
    O4 = Observer(O3)

    chain = [O1, O2, O3, O4]

    result = generate_key_path(chain)
    print("Key Path:", result["path"])
    print("Generated Key:", result["key"])

    visualize_observer_chain(chain)
