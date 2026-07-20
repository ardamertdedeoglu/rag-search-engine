import argparse

from lib.semantic_search import (
    embed_query_text,
    embed_text,
    semantic_search,
    verify_embeddings,
    verify_model,
    chunk_text,
    semantic_chunk_text,
    embed_chunks_command,
    search_chunked_command
)

from lib.search_utils import (
    DEFAULT_CHUNK_SIZE,
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_SEMANTIC_CHUNK_SIZE,
    DEFAULT_SEARCH_LIMIT
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("verify", help="Verify that the embedding model is loaded")

    single_embed_parser = subparsers.add_parser(
        "embed_text", help="Generate an embedding for a single text"
    )
    single_embed_parser.add_argument("text", type=str, help="Text to embed")

    subparsers.add_parser(
        "verify_embeddings", help="Verify embeddings for the movie dataset"
    )

    embed_query_parser = subparsers.add_parser(
        "embed_query", help="Generate an embedding for a search query"
    )
    embed_query_parser.add_argument("query", type=str, help="Query to embed")

    search_parser = subparsers.add_parser(
        "search", help="Search for movies using semantic search"
    )
    search_parser.add_argument("query", type=str, help="Search query")
    search_parser.add_argument(
        "--limit", type=int, default=5, help="Number of results to return"
    )

    chunk_parser = subparsers.add_parser("chunk", help="Split a text into chunks")
    chunk_parser.add_argument("query", type=str, help="Text to split")
    chunk_parser.add_argument(
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help="Number of chunks to split",
    )
    chunk_parser.add_argument(
        "--overlap",
        type=int,
        default=DEFAULT_CHUNK_OVERLAP,
        help="Amount of words to overlap",
    )

    semantic_chunk_parser = subparsers.add_parser(
        "semantic_chunk", help="Semantically split a text into chunks"
    )
    semantic_chunk_parser.add_argument("query", type=str, help="Text to split")
    semantic_chunk_parser.add_argument(
        "--max-chunk-size",
        type=int,
        default=DEFAULT_SEMANTIC_CHUNK_SIZE,
        help="Amount of sentences to split",
    )
    semantic_chunk_parser.add_argument(
        "--overlap",
        type=int,
        default=DEFAULT_CHUNK_OVERLAP,
        help="Amount of sentences to overlap",
    )
    
    subparsers.add_parser("embed_chunks", help="Embed movie chunks")
    
    chunked_search_parser = subparsers.add_parser("search_chunked", help="Search with chunked movies")
    
    chunked_search_parser.add_argument("query", type=str, help="Text to search")
    chunked_search_parser.add_argument("--limit", type=int, default=DEFAULT_SEARCH_LIMIT, help="Limit the search results")
    

    args = parser.parse_args()

    match args.command:
        case "verify":
            verify_model()
        case "embed_text":
            embed_text(args.text)
        case "verify_embeddings":
            verify_embeddings()
        case "embed_query":
            embed_query_text(args.query)
        case "search":
            semantic_search(args.query, args.limit)
        case "chunk":
            chunk_text(args.query, args.chunk_size, args.overlap)
        case "semantic_chunk":
            semantic_chunk_text(args.query, args.max_chunk_size, args.overlap)
        case "embed_chunks":
            embed_chunks_command()
        case "search_chunked":
            search_chunked_command(args.query, args.limit)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
