"""CLI wrapper for the idempotent feature-engineering pipeline step."""
import argparse,logging
from pathlib import Path
from .features import save_features

def run(input_path,output_path):
    """Generate the project feature table and log the checkpoint."""
    logging.info("Reading %s",input_path); result=save_features(input_path,output_path); logging.info("Wrote %s",result); return result

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--input",default="project/data/processed/multi_asset_market_data_processed.csv"); parser.add_argument("--output",default="project/data/processed/market_features.csv"); args=parser.parse_args(); logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s"); run(Path(args.input),Path(args.output))
if __name__=="__main__": main()
