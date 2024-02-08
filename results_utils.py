def create_results_directory(directory=results_directory):
    if not os.path.exists(directory):
        os.mkdir(directory)