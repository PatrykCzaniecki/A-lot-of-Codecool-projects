using UnityEngine;

namespace DungeonCrawl.Core
{
    /// <summary>
    ///     Class used for manipulating camera's position
    /// </summary>
    public class CameraController : MonoBehaviour
    {
        /// <summary>
        ///     CameraController singleton
        /// </summary>
        public static CameraController Singleton { get; private set; }

        /// <summary>
        ///     Camera's current position
        /// </summary>
        public (int x, int y) Position
        {
            get => _position;
            set
            {
                _position = value;
                transform.position = new Vector3(value.x, value.y, -10);
            }
        }

        /// <summary>
        ///     Camera's size (how much space can it see)
        /// </summary>
        public float Size
        {
            get => _camera.orthographicSize;
            set => _camera.orthographicSize = 4;
        }

        private (int x, int y) _position;
        public Camera _camera;

        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;

            _camera = GetComponent<Camera>();
        }
    }
}
